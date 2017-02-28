---
layout: post
title: "xv6中存储cpu和进程信息的技巧"
description: "xv6中存储cpu和进程信息的技巧"
keywords: "xv6, cpu, multiprocess, OS"
category: OS
tags: [OS,xv6]
---
{% include JB/setup %}

> xv6中存储cpu和进程信息的技巧

`xv6`是一个支持多处理器的`Unix-lik`操作系统，

近日阅读源码时发现`xv6`在记录当前CPU和进程状态时非常tricky

首先，上代码：

```C
 1 extern struct cpu cpus[NCPU];
 2 extern int ncpu;
 3 
 4 // Per-CPU variables, holding pointers to the
 5 // current cpu and to the current process.
 6 // The asm suffix tells gcc to use "%gs:0" to refer to cpu
 7 // and "%gs:4" to refer to proc.  seginit sets up the
 8 // %gs segment register so that %gs refers to the memory
 9 // holding those two variables in the local cpu's struct cpu.
10 // This is similar to how thread-local variables are implemented
11 // in thread libraries such as Linux pthreads.
12 extern struct cpu *cpu asm("%gs:0");       // &cpus[cpunum()]
13 extern struct proc *proc asm("%gs:4");     // cpus[cpunum()].proc
```
 

其中`struct cpu`是一个用来保存每个cpu运行状态的结构体，

代码第一行定义了结构体数组`cpus[NCPU]`，`NCPU`对应`cpu`的总数（最大为`8`），也就是说`cpus`用来存储所有cpu的运行状态。


**那么问题来了：**
**`上面的内核代码是运行于每个cpu之中的，那每个cpu如何知道自身的当前运行状态呢？`**

对于这个问题，我们可以通过`lapic`获取cpu自身编号，再利用编号对`cpus`寻址即可，

也就是说，对于任意一个`cpu`，自身状态的存储位置可以这样获得： 
```C
struct cpu *c = &cpus[cpunum()]; 
```

**然而，第二个问题来了：**
**`我们不可能每次引用cpu自身状态时都通过lapic获取编号啊，能不能弄一个全局变量把状态位置一次性存储下来呢？`**
**`像是这样， struct cpu *cpu; //全局变量，存储cpu自身状态，`**
**`然后在初始化代码中 cpu = c；`**

**`对于记录每个cpu正在运行的进程也有这样的问题，能不能写成：`**
**`struct proc *proc; //全局变量，存储当前cpu正在运行的进程状态`**

 
**那么，第三个问题来了：**
**`每个cpu是独立并行的，在每个cpu上运行的内核代码都是一样的，页表也一样，`**
**`这意味着全局变量cpu和proc的地址也是一样的，这样便不可以用来区分不同cpu的状态了。`**
**`因此，我们需要一种方法，可以让我们在每个cpu中都用同一个符号记录状态，但这些符号却是映射到不同的地址。`**

既然页表一样，我们自然不能用一个绝对的数值来寻址啦，仔细想想，页表之上有什么？页表之上，还有`段表`啊。

所以我们需要用`segment register`来寻址，只要我们在建立段表时把该段都映射到不同的内存区域不就可以了，所以我们有了以下声明：
```C
1 extern struct cpu *cpu asm("%gs:0");       // &cpus[cpunum()]
2 extern struct proc *proc asm("%gs:4");     // cpus[cpunum()].proc
```
我们用`gs`作为段寄存器，`cpu`指向`[%gs]`，`proc`指向`[%gs+4]`，

其中为什么开头要用`extern`呢？我问过某大神，他说是因为`gs段`是在外部建立的，相当于外部定义的。。。

 

**OK，最后一个问题来了，**
**`gs段应该指向哪，才能确保每个cpu的gs段都位于不同的区域？`**

最直观的想法当然是指向对应的`cpus[num]`内部啦，所以在`struct cpu`尾部增加两个域：

```C
1 struct cpu{
2    ........  //cpu状态
3 
4    // Cpu-local storage variables; see below
5   struct cpu *cpu;
6   struct proc *proc;           // The currently-running process.
7 }
```

然后在建立段表时，增加`gs段`，并映射至尾部这两个域：

```C
 1   c = &cpus[cpunum()];
 2   
 3   ......... //建立其他段
 4 
 5   // 建立gs段，共两个域（存储cpu和proc地址），起始地址为&c->cpu
 6   c->gdt[SEG_KCPU] = SEG(STA_W, &c->cpu, 8, 0);
 7 
 8   //加载gdt
 9   lgdt(c->gdt, sizeof(c->gdt));
10   //加载gs
11   loadgs(SEG_KCPU << 3);
12   
13   // 把当前cpu和proc状态的地址赋给cpu和proc全局变量
14   //而cpu变量实质为%gs:0, proc变量实质为%gs:4
15   cpu = c;
16   proc = 0;
```
 

其实在这里`cpu`和`proc`变量跟线程局部存储的性质差不多，每个处理器都可以引用同一个变量，但这些变量都对应不同的存储区域。

有可能这种实现技巧跟`TLS（线程局部存储）`差不多，有空研究下`TLS`的实现看看是不是。

# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!


At a first glance, I was pleasantly surprised with the problem and excited to get started finding a solution as I am a student who has previously taken a few biology and chemistry courses. Yet, as with any problem I encounter, I start with a simple google search to curiously dive deeper into what exactly a circular genome map represents and what I need to know before I can even think about solving the problem. After a few hours of research, I know enough to get started implementing a solution and the first thing I do is visualize how I would represent a circular genome map as a png using a programming language. 

At first, I think of going the simpler path and coding it in Java or C++, which are languages I am familiar with. Yet, as I dive deeper, I find a library called **BioPython**, which seems like a great way to represent biology using programming. I realize that even though I am not familiar with python, and that it would be difficult to learn in a few days, I am not disheartened and remain calm. I research more on python and the biopython library over the next few days and discover that I would need a library to convert the given Genbank to a png and end up finding ReportLab. This makes the programming tremendously more efficient as it saves me the trouble to write a program that can convert a file to a png image. In addition, I learned how to read in a Genbank file using the SeqIo.read function supported by python, which reads in sequences from a given file and can transform them into something readable to the computer, such as strings. 

Next, I create an empty genome diagram, feature sets, and a track for feature sets. I iterate over the Genbank file looking for the features of the virus that are genes, and color code them differently into my circular genome diagram. For illustration purposes, I attempt to find EcoRI recognition sites in the Genbank file (taken from the examples in https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html) and output the png file. In the end, I enjoyed this project even though this challenge was harder than it seemed and learned something new at the end of the day, and that is what matters the most to me.

Sources: https://biopython.org/
         https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html (how to create empty diagram, set, features, and readin from genbank file)
         https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html


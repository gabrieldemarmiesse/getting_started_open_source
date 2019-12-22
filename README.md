# Getting started with open-source
You want to make a pull request to an open-source project? You don't know how to do it? Here is how to.

This guide will show you how to make a contribution (modifying code, adding things in the docs...) to an open source project that you don't own.

### This guide will suppose that:

1) You know how to use git, at least you know what is a commit and a branch and a few basic commands.
2) You know which project you to work on. In this guide, we'll assume that it's an open source project that you don't control and that the repository is hosted on GitHub. For example, it could be [Cython](https://github.com/cython/cython), [the Windows terminal](https://github.com/microsoft/terminal) or [Tensorflow](https://github.com/tensorflow/tensorflow).
3) You know what modification you want to do. What I mean is that you know which file you want to modify and which lines.

In here, we'll always take as example my account: https://github.com/gabrieldemarmiesse and we'll say that I want to make a contribution to autokeras (https://github.com/keras-team/autokeras).

### Step 1: Making a fork

First head to the page of the project, in my example, autokeras: https://github.com/keras-team/autokeras . If you look at the top right of the page, you'll see a button called "Fork":
 
 ![](./screenshots/fork_button.png)
 
 Click on it and create your fork. It will redirect you to your fork.
 
 #### What is a fork?
 
 In short, a fork is a copy of a repository. In our case, the repository is https://github.com/keras-team/autokeras , if I make a fork of it, I'll have a copy at https://github.com/gabrieldemarmiesse/autokeras . It'll be one of my repositories. Since it's my own repository now, I can pull and push as much as I want. 
 
 ### Step 2: Cloning your fork
 
 I now have my fork of autokeras under my username: https://github.com/gabrieldemarmiesse/autokeras . I'll use it to work since I can push and pull to it. Click on the green "Clone" button (of your fork, not the original repository) and use it to clone locally. For example, in my case, I can do:
 
 ```bash
git clone https://github.com/gabrieldemarmiesse/autokeras.git
```

to clone with HTTPS or 

```bash
git clone git@github.com:gabrieldemarmiesse/autokeras.git
```

to clone it with SSH.

### Step 3: 

...
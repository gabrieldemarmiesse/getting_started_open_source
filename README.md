# Getting started with open-source
You want to make a pull request to an open-source project? You don't know how to do it? Here is how to.

This guide will show you how to make a contribution (modifying code, adding things in the docs...) to an open source project that you don't own.

### This guide will assume that:

1) You know how to use git, at least you know what is a commit and a branch and a few basic commands.
2) You know which project you want to work on. In this guide, we'll assume that it's an open source project that you don't control and that the repository is hosted on GitHub. For example, it could be [Cython](https://github.com/cython/cython), [the Windows terminal](https://github.com/microsoft/terminal) or [Tensorflow](https://github.com/tensorflow/tensorflow).
3) You know what modification you want to do. What I mean is that you know which file you want to modify and which lines.

In here, we'll always take as example my account: https://github.com/gabrieldemarmiesse and we'll say that I want to make a contribution to autokeras (https://github.com/keras-team/autokeras).

### Step 1: Making a fork

First head to the page of the project, in my example, autokeras: https://github.com/keras-team/autokeras . If you look at the top right of the page, you'll see a button called "Fork":
 
 ![](./screenshots/fork_button.png)
 
 Click on it and create your fork. It will redirect you to your fork.
 
 #### What is a fork?
 
 In short, a fork is a copy of a repository. In our case, the repository is https://github.com/keras-team/autokeras (upstream), if I make a fork of it, I'll have a copy at https://github.com/gabrieldemarmiesse/autokeras . It'll be one of my repositories. Since it's my own repository now, I can pull and push as much as I want. When people talk about fork, they also talk about the upstream repository (original repository). You'll see later how to update your fork with commits for the upstream repository.
 
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

### Step 3: Make a new branch to work on you feature

It's never a good idea to work on the master branch. It'll become clear why once you start doing your second pull request. So let's make a new one:
```bash
cd ./autokeras
git checkout -b my_pretty_branch_for_pr_1
git status
```

You're now on the new branch `my_pretty_branch` and ready to work! 

Remember: one branch = one pull request. The branch name doesn't have to be the name of your pull request, so no worries if your branch name is bad or not very descriptive.

### Step 4: Modify the code/docs

Find the file you want to modify and modify it. Change the code, etc... I won't detail here how to run the test suite as it's optional in open source projects. Especially if the modification is small. A server will run some tests for you anyway. So let's go on.

### Step 5: Push your branch

This is quite simple:
```bash
git add .
git commit
git push
```

If you go to your fork (in our case https://github.com/gabrieldemarmiesse/autokeras), you'll see that your branch is now there (you can click on the branch button to see).


### Step 6: Opening the pull request

Now head to the original repository. Click on the tab "Pull requests", you should see a banner saying something like "You just pushed the xxx branch 2 minutes ago. Make a pull request?". 

Click the green button and you'll be able to review the diff, add a title to your pull request and add a description. 

Don't worry, you'll be able to modify the pull request later on. If you think that you forgot a modification in the code or you later on wants to change the title, it's fine.


### Step 7: The continuous integration system

Every time you open a pull request, it will trigger tests in a CI system.

You can see the CI and the logs at the bottom of the pull request:

 ![](./screenshots/continuous_integration.png)

If the CI is failing, you can see why by checking the logs. For that, click on "Details".

#### What is a CI system?

CI stands for "Continuous integration". It's a system that runs on a server. It watches your git repository closely. 

Every time you add a commit to the repository, or every time a pull request is opened, the CI system will spawn a fresh new virtual machine, clone the repository, checkout to the commit that was just added and runs many tests. It then reports the result.


### Step 8 (optional): Add more commits to your pull request

The pull request is now done, but there is still the code review. You might need to wait for a few days until a maintainer reviews your code. 

Once the maintainer does, if everything is good, you'll get some thanks and your pull request will be merged.

If the maintainer ask for changes (which is frequent), you need to modify the code. In this case **do not open another pull request**. As was said earlier, one branch = one pull request. You just need to do:

```bash
git checkout my_pretty_branch_for_pr_1
```
In case you were not on this branch already. 

Then do the requested code modifications and do:

```bash
git add .
git commit
git push
```

The commit will be added to the branch. You should see it appear in the pull request page. You'll also trigger the continuous integration system again with this new commit.

Repeat step 8 until your pull request is merged!



### Step 9: Make a second pull request

Your first pull request was merged. Maybe you think it was easier than you thought and you'd like to do it again.

You may be very tempted to delete your fork and redo steps 1 to 8 again. 
It's obvious that there is a better solution...

#### Sync your local master branch with the upstream master branch

If you remember, we said earlier that working on the master branch wasn't a good idea. You'll understand why now. We need the master branch to be in sync with the upstream master branch.


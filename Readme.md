![psi](https://github.com/zstreeter/CHEM-210A-2020/blob/master/images/psi.png)

# Quantum Chemistry: CHEM 210 A 2020

# Python Setup

- Download Anaconda if you haven't already
  https://www.anaconda.com/distribution/

  - Make sure conda is installed and in your \$PATH by looking at this command's
    output.

    ```shell
    conda --version
    ```

    Can check if \$PATH environment variable is pointing to the spot you
    installed Anaconda via this command:

    ```shell
    echo $PATH
    ```

- Checkout this site for installing Psi4 with Anaconda
  http://www.psicode.org/psi4manual/1.1/conda.html

  - Before doing anything else, update conda!

    ```shell
    conda update --all
    ```

  - Create virtual environment for Psi4

    ```shell
    $ conda create -n Psi4env python=3.7 psi4 psi4-rt -c psi4
    ```

  * Now can use this environment with the command

    ```shell
      (base) $ conda activate Psi4env
    ```

    and deactivate it with

    ```shell
       (Psi4env) $ conda deactivate
    ```

  - To add other packages (e.g. matplotlib) within your new virtual environment
    issue this command

    ```shell
       (Psi4env) $ conda install matplotlib
    ```

    The bare bones Psi4 environment may not have some packages we will use so
    this may be required if Spyder cannot find the module.

- If you use an IDE like Spyder, then you need to install Spyder within your
  virtual environment.

  - So activate your environment like above and then install Spyder

    ```shell
      (Psi4env) $ conda install spyder
    ```

  - Now still _within_ your virtual environment invoke spyder.

    ```shell
       (Psi4env) $ spyder
    ```

    Now you will be working inside of the Spyder IDE and have everything that's
    in the Psi4 environment!

- Another useful IDE **and voted number 1 for python** is Pycharm. This IDE has
  a larger learning curve and that usually means it will benefit you in the long
  run if you adopt this as your main editor. I know most professionals in
  industry swear by it and I am pretty sure the professional version is free for
  students!
  - https://www.jetbrains.com/pycharm/promo/anaconda/
  - Here is an example setting up a virtual environment in Pycharm
    https://medium.com/infinity-aka-aseem/how-to-setup-pycharm-with-an-anaconda-virtual-environment-already-created-fb927bacbe61

# Unix Setup

- You MUST install Scone! It will give you all the developer programs you will
  need in the terminal. https://apps.apple.com/us/app/xcode/id497799835?mt=12
- Package managers are extremely helpful and for Mac OS we will use MacPorts.
  https://www.macports.org/install.php.
- Installing Molden via MacPorts

```shell
  $ sudo port install molden
```

# Windows Setup (Requires Windows 10)

- First, setup Windows Subsystem Linux (WSL) to get the Linux bash shell by
  following this site:
  https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/
- Second, setup an X-server so we can use Molden. For Windows there is a program
  called Xming; follow this site for setup steps:
  https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/
  - Run this command to set your enviroment to always launch the X-server
    correctly:

```shell
  $ echo "export DISPLAY=:0" >> ~/.bashrc
```

Now we have a Windows developer setup!

- Now lets download Molden and install:
  http://cheminf.cmbi.ru.nl/molden/molden.html
  1. Go to your new linux bash prompt.
  2. Find the downloaded Molden .tar file
  3. Untar the file

```shell
  $ tar -xvf molden_file_name.tar
```

4. Go inside molden folder

```shell
  $ cd molden_file_name
```

5. Type the command

```shell
  $ make molden
```

6. Now type the command

```shell
  $ make install
```

If you get errors in this process, please let me know.

- To get Psi4 working, we found a channel for Psi4 on Windows
  https://anaconda.org/raimis/psi4. So just need to issue this command in your
  Psi4 environment:

```shell
 (Psi4env) $ conda install -c raimis psi4
```

# Psi4

- http://www.psicode.org/psi4manual/1.2/index.html

# Slack

- Coming Soon!

# Useful Unix/Linux Terminal Commands

- I found this website that mentions some of the most used commands so have a
  look! https://learntocodewith.me/command-line/unix-command-cheat-sheet/

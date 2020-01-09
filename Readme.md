![](https://github.com/zstreeter/CHEM-210A-2020/blob/master/images/psi.png = 250x)

Quantum Chemistry: CHEM 210 A 2020
=========

# Python Setup
* Download Anaconda if you haven't already https://www.anaconda.com/distribution/
  * Make sure conda is installed and in your \$PATH by looking at this command's output.

    ```shell
	$ conda --version 
    ```

    Can check if \$PATH environment variable is pointing to the spot you installed Anaconda via this command:

    ```shell
	$ echo $PATH
    ```

* Checkout this site for installing Psi4 with Anaconda http://www.psicode.org/psi4manual/1.1/conda.html
  * Before doing anything else, update conda!

    ```shell
	$ conda update --all
    ```

  * Create virtual environment for Psi4

    ```shell
	$ conda create -n Psi4env python=3.7 psi4 psi4-rt -c psi4
    ```
  - Now can use this environment with the command

    ```shell
      (base) $ conda activate Psi4env
    ```
    and deactivate it with

    ```shell
       (Psi4env) $ conda deactivate
    ```
* If you use an IDE like Spyder, then you need to install Spyder within your virtual environment.
  * So activate your environment like above and then install Spyder

    ```shell
      (Psi4env) $ conda install spyder
    ```
  * Now still *within* your virtual environment invoke spyder.

    ```shell
       (Psi4env) $ spyder
    ```
    Now you will be working inside of the Spyder IDE and have everything that's in the Psi4 environment!
*  To add other packages (e.g. matplotlib) within your new virtual environment issue this command:

    ```shell
       (Psi4env) $ conda install matplotlib
    ```
   The bare bones Psi4 environment may not have some packages we will use so this may be required if Spyder cannot find the module. 

* Another useful IDE **and voted number 1 for python** is Pycharm. This IDE has a larger learning curve and that usually means it will benefit you in the long run if you adopt this as your main editor. I know most professionals in industry swear by it and I am pretty sure the professional version is free for students!
  * https://www.jetbrains.com/pycharm/promo/anaconda/
  * Here is an example setting up a virtual environment in Pycharm https://medium.com/infinity-aka-aseem/how-to-setup-pycharm-with-an-anaconda-virtual-environment-already-created-fb927bacbe61 

# Unix Setup
* I found some of you do not have Xcode so you MUST install this! It will give you all
  the developer programs you will need in the terminal. 
  https://apps.apple.com/us/app/xcode/id497799835?mt=12
* Package managers are extremely helpful and for Mac OS we will use MacPorts.
  https://www.macports.org/install.php.
* Installing Molden via MacPorts

    ``````shell
      $ sudo port install molden
    ``````

# Windows Setup (Requires Windows 10)
* First, setup Windows Subsystem Linux (WSL) to get the Linux bash shell by following this site:
  https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/
* Second, setup an X-server so we can use Molden. For Windows there is a program called Xming; follow this site for setup steps:
  https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/
Now we have a Windows developer setup!
* Now lets download Molden and install: http://cheminf.cmbi.ru.nl/molden/molden.html
  1. Go to your new linux bash prompt.
  2. Find the downloaded Molden .tar file
  3. Untar the file "tar -xvf molden_file_name.tar"
  4. Go inside molden folder "cd molden_file_name"
  5. Type the command "make molden"
  6. Now type the command "make install"
* To get Psi4 working, we found a channel for Psi4 on Windows https://anaconda.org/raimis/psi4.
  So just need to issue this command in your Psi4 environment:

    ``````shell
     (Psi4env) $ conda install -c raimis psi4
    ``````

# Psi4
* http://www.psicode.org/psi4manual/1.2/index.html

# Slack
* Say what's up! https://join.slack.com/t/chem210a/shared_invite/enQtODk2NTkwNjc5MDI4LWZkMDc4ZTQ5YzcxZTY3NmZkN2JmZTBhYmQ4YzU0NGE1YzdiMzE5YTRlM2I2NTVlMWZkZThlMDgwYTBiMTIzNzA

# Useful Unix/Linux Terminal Commands
* I found this website that mentions some of the most used commands so have a look!
  https://learntocodewith.me/command-line/unix-command-cheat-sheet/

<!-- #### Computer language, intro to architecture -->
<!-- * example `n**2` (1) Python -->

<!-- ```python -->
<!-- n = 5 -->
<!-- n ** 2 -->
<!-- ``` -->
<!-- (2) Assembly -->

<!-- ```assembly -->
<!-- push rbp -->
<!-- mov rbp, rsp -->
<!-- mov DWORD PTR [rbp-4], edi -->
<!-- mov eax, DWORD PTR [rbp-4] -->
<!-- imul eax, DWORD PTR [rbp-4] -->
<!-- pop rbp -->
<!-- ret -->
<!-- ``` -->
<!-- * registers and aritmetic units, (3) Binary -->

<!-- ```binary -->
<!-- 011100000111010101110011011010000010000001110010011000100 -->
<!-- 1110000000010100110110101101111011101100010000001110010011 -->
<!-- 0001001110000001011000010000001110010011100110111000000001 -->
<!-- 0100110110101101111011101100010000001000100010101110100111 -->
<!-- 1010100100100010000100000010100000101010001010010001000000 -->
<!-- 1011011011100100110001001110000001011010011010001011101001 -->
<!-- 0110000100000011001010110010001101001000010100110110101101 -->
<!-- 1110111011000100000011001010110000101111000001011000010000 -->
<!-- 0010001000101011101001111010100100100010000100000010100000 -->
<!-- 1010100010100100010000001011011011100100110001001110000001 -->
<!-- 0110100110100010111010000101001101001011011010111010101101 -->
<!-- 1000010000001100101011000010111100000101100001000000100010 -->
<!-- 0010101110100111101010010010001000010000001010000010101000 -->
<!-- 1010010001000000101101101110010011000100111000000101101001 -->
<!-- 1010001011101000010100111000001101111011100000010000001110 -->
<!-- 010011000100111000000001010011100100110010101110100 -->
<!-- ``` -->
<!-- * interpreted vs compiled -->
<!-- * LLVM -->

<!-- #### Variables, intro to code standards -->
<!-- * float, int, numpy arrays -->
<!-- * code standards -->
<!--   * constants -->
<!--   * tabs -->
<!--   * capital letters -->
<!--   * comments -->
<!--   * extra `\n` -->
<!--   * meaningful names -->

<!-- #### Basic variables, intro to code design -->
<!-- * functions, ```DRY``` code, default value in a function -->
<!-- * lists, dynamic memory allocation -->

<!-- ## Scientific Python -->
<!-- #### Intro to `numpy` -->
<!-- * numpy, lapack, blas, mkl -->
<!-- * basic numpy, the importance of knowing the size of the variable -->
<!-- * eigenvalues, eigenvectors, transformation -->
<!-- * debugging part 1, variable states -->
<!-- * matrix exp -->
<!-- * changing a basis set (next time fftw) -->
<!-- * debugging part 2: reusing existing code, change variable states, the `?` operator -->
<!-- * scipy and runge kutta -->
<!-- * solving a 2 level system with Runge-Kutta -->
<!-- * Problem: 3LS, see here: http://community.dur.ac.uk/thomas.billam/JQC_Atom_Light_2015-2016_L7.pdf -->

<!-- # Part 2 -->
<!-- * OOP -->
<!-- * fftw -->
<!-- * matplotlib -->
<!-- * unit tests? -->

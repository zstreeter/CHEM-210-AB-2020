Quantum Chemistry: CHEM 210 A
=========

# Python Setup
* download Anaconda if you haven't already https://www.anaconda.com/distribution/
* Checkout this site for installing Psi4 with Anaconda http://www.psicode.org/psi4manual/master/tutorial.html
  * Though, we just need to create virtual environment for Psi4

    ```shell
	$ conda create -n Psi4env python=3.7 psi4 psi4-rt -c psi4
    ```
  - Now can use this environment with the command

    ```shell
        $ conda activate Psi4env
    ```
    and deactivate it with

    ```shell
        $ conda deactivate
    ```
* If you use an IDE like Spyder, then you need to install Spyder within your virtual environment.
  * So activate your environment like above and then install Spyder

    ```shell
        $ conda install spyder
    ```
  * Now still *within* your virtual environment invoke spyder.

    ```shell
        $ spyder
    ```
    Now you will be working inside of the Spyder IDE and have everything that's in the Psi4 environment!

# Unix Setup
* Package managers are extremely helpful and there are two for Mac OS, MacPorts
  and Homebrew.
  I use MacPorts and you can install it from here https://www.macports.org/install.php.
  Homebrew is very popular and is easy to use with similar commands to MacPorts,
  http://osxdaily.com/2018/03/07/how-install-homebrew-mac-os/.
* Installing Molden for MacPorts

    ``````shell
      sudo port install molden
    ``````

  The installation using Homebrew is probably similar

    ``````shell
      $ brew install molden
    ``````

# Windows Setup
* Just need to get Molden differently (I believe) http://cheminf.cmbi.ru.nl/molden/howtoget.html

# Psi4
* http://www.psicode.org/psi4manual/1.2/index.html

# Slack
* Say what's up! https://join.slack.com/t/chem210a/shared_invite/enQtODk2NTkwNjc5MDI4LWZkMDc4ZTQ5YzcxZTY3NmZkN2JmZTBhYmQ4YzU0NGE1YzdiMzE5YTRlM2I2NTVlMWZkZThlMDgwYTBiMTIzNzA

#### Computer language, intro to architecture
* example `n**2` (1) Python
```python
n = 5
n ** 2
```
(2) Assembly
```assembly
push rbp
mov rbp, rsp
mov DWORD PTR [rbp-4], edi
mov eax, DWORD PTR [rbp-4]
imul eax, DWORD PTR [rbp-4]
pop rbp
ret
```
* registers and aritmetic units, (3) Binary
```binary
011100000111010101110011011010000010000001110010011000100
1110000000010100110110101101111011101100010000001110010011
0001001110000001011000010000001110010011100110111000000001
0100110110101101111011101100010000001000100010101110100111
1010100100100010000100000010100000101010001010010001000000
1011011011100100110001001110000001011010011010001011101001
0110000100000011001010110010001101001000010100110110101101
1110111011000100000011001010110000101111000001011000010000
0010001000101011101001111010100100100010000100000010100000
1010100010100100010000001011011011100100110001001110000001
0110100110100010111010000101001101001011011010111010101101
1000010000001100101011000010111100000101100001000000100010
0010101110100111101010010010001000010000001010000010101000
1010010001000000101101101110010011000100111000000101101001
1010001011101000010100111000001101111011100000010000001110
010011000100111000000001010011100100110010101110100
```
* interpreted vs compiled
* LLVM

#### Variables, intro to code standards
* float, int, numpy arrays
* code standards
  * constants
  * tabs
  * capital letters
  * comments
  * extra `\n`
  * meaningful names

#### Basic variables, intro to code design
* functions, ```DRY``` code, default value in a function
* lists, dynamic memory allocation

## Scientific Python
#### Intro to `numpy`
* numpy, lapack, blas, mkl
* basic numpy, the importance of knowing the size of the variable
* eigenvalues, eigenvectors, transformation
* debugging part 1, variable states
* matrix exp
* changing a basis set (next time fftw)
* debugging part 2: reusing existing code, change variable states, the `?` operator
* scipy and runge kutta
* solving a 2 level system with Runge-Kutta
* Problem: 3LS, see here: http://community.dur.ac.uk/thomas.billam/JQC_Atom_Light_2015-2016_L7.pdf

# Part 2
* OOP
* fftw
* matplotlib
* unit tests?

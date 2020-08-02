# concat_pdf

[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://app.circleci.com/pipelines/github/ikanago/concat_pdf)

Docker image to concatenate separated PDF files into one file without untrustworthy third-party service or Adobe subscription.

## How to Run
1. Pull docker image.

```
$ docker pull ikanag0/concat_pdf
```

2. Prepare files to merge

To merge PDF files properly, you have to give a serial number for each file.  
For example, your input files should be like this:
```
$ ls files
img001.pdf  imag002.pdf  ... img010.img  img011.img
```

3. Run following command

```
$ docker run --rm -v "`pwd`:/data" ikanag0/concat_pdf:latest files
$ ls
files  output.pdf
```
You will get `output.pdf` merged in the order of the serial numbers of these files.  
You can change an output file name with `-o` option.

## Recommended Setting

You can set an alias to this command.
```
alias concat_pdf='docker run --rm -v "`pwd`:/data" ikanag0/concat_pdf:latest'

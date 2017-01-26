## Research Project GUI - Austin Brown

### Requirements
- Python 2.7.10 or above
- virtualenv
```sh
$ pip install virtualenv
```
---
### Instructions
Once you have virtualenv installed,
```sh
$ virtualenv venv
```
```sh
$ source venv/bin/activate
```
You should then see a `(venv)` to the left of your working directory.

To install the dependencies for this project,
```sh
$ pip install -r requirements.txt
```
After these are installed, simply run
```sh
$ python graph.py
```
and you should see an icon pop up where the GUI is running.

### Usage

Currently, the way to read in files is to convert `.mat` files to `.csv`. This can be easily accomplished in MATLAB using `csvwrite()`:

```sh
>> load('FileName.mat')
>> csvwrite('in.csv', FileName) 
```

Once this is done, copy the `.csv` file to the root directory of this project. It is expecting the file `in.csv`, so do not change the name. In future iterations, there will be the option to upload any `.csv` file.

### Questions and contributing
This project is lincensed under the [MIT License](https://opensource.org/licenses/MIT) (see license.txt). If you want to contribute, please fork this repository, go crazy with it, and then submit a pull request and I promise I'll respond!  
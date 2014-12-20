[![Build Status](https://travis-ci.org/diegotoral/SaltShaker.svg?branch=master)](https://travis-ci.org/diegotoral/SaltShaker)[![Latest Version](https://pypip.in/version/saltshaker/badge.svg?text=version)](https://pypi.python.org/pypi/saltshaker/)[![Downloads](https://pypip.in/download/saltshaker/badge.svg?period=day|week|month)](https://pypi.python.org/pypi/saltshaker/)[![License](https://pypip.in/license/saltshaker/badge.svg)](https://pypi.python.org/pypi/saltshaker/)

SaltShaker
==========

Development environment provisioning with Salt made easy. Just **Shaker** it!

*Shaker* is developed with `Python` and aims to be simple and fast to start using. *Shaker* uses [Salt](https://github.com/saltstack/salt) to provision your workstation. It reads *salt formules* from an *Git* repository (or from local directories).

## Installation ##

To install *Shaker* use `pip`.

```sh
$ pip install saltshaker
```

## Usage ##
### Creating a config file ###

*Shaker* `init` command can be used to start a new configuration file within the current directory.

```sh
$ shaker init
```

### Running Shaker ###

Running *Shaker* is really simple.

```sh
$ shaker
```

## Configuration ##

*Shaker* uses [YAML](http://www.yaml.org/) to its configuration file `.shaker.yml`. This file lists sources and specify overrides for the main `top.sls` file.

```yaml
sources:
  local:
    - /home/diegotoral/salt/formules
    - /salt/
  git: https://github.com/diegotoral/saltshaker-formules
  
top:
  base:
    - rvm
    - vim
```
### Configuration Options ###
#### sources ####
Specify Where *Shaker* must look for Salt formules.

##### Avaliable options #####
**local**
: List where to look for Salt formules on the local filesystem.

**git**
: A Git repository to download and use as a source for Salt formules.

#### top ####
Allows you to override the `top.sls` file from the sources. The `top` parameter and `top.sls` are merged and the resulting configuration is executed.

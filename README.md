[![Build Status](https://travis-ci.org/diegotoral/SaltShaker.svg?branch=master)](https://travis-ci.org/diegotoral/SaltShaker) [![Latest Version](https://pypip.in/version/saltshaker/badge.svg?text=version)](https://pypi.python.org/pypi/saltshaker/) [![Downloads](https://pypip.in/download/saltshaker/badge.svg?period=day|week|month)](https://pypi.python.org/pypi/saltshaker/) [![License](https://pypip.in/license/saltshaker/badge.svg)](https://pypi.python.org/pypi/saltshaker/) [![Coverage Status](https://img.shields.io/coveralls/diegotoral/SaltShaker.svg)](https://coveralls.io/r/diegotoral/SaltShaker)

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

*Shaker* `init` command can be used to start a new configuration file.

```sh
$ shaker init
```

A configuration file will be created at `$HOME/.shaker/config.yml`.

### Running Shaker ###

When configuration is done you can start *Shaker*.

```sh
$ shaker
```

*Shaker* will read the configuration from `$HOME/.shaker/config.yml` and start provisioning the machine.

## Configuration ##

*Shaker* configuration files are simple [YAML](http://www.yaml.org/) files. The configuration tells Shaker where to find `salt formules` to use.

```yaml
sources:
  local:
    - /home/diegotoral/salt/formules
    - /tmp/formules
  git: https://github.com/diegotoral/saltshaker-formules

top:
  base:
    - rvm
    - vim
```

### Configuration Options ###
#### sources ####

By default *Shaker* looks for `salt formules` at `$HOME/.shaker/formules`. The `sources` option allows you to specify other places where *Shaker* may find formules.

##### local #####

Directories where to look for salt formules on the local filesystem.

##### git ####

Git repository url to download and use as a `source`.

#### top ####

Allows you to override the `top.sls` file from the sources. The `top` parameter and `top.sls` are merged and the resulting configuration is executed.

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

*Shaker* configuration... [YAML]().

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
Where to find salt formules.

#### top ####
Allows you to override the `top.sls` file from the sources. The `top` parameter and `top.sls` are merged and the resulting configuration is executed.

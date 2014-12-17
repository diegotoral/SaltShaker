SaltShaker
==========

Development environment provisioning with Salt made easy. Just **Shaker** it!

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

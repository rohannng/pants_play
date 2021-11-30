# Introduction 
Pants Playground

# Pants Bootstraping

> Note - this section has already been done for this Repo

Check [pants Installation](https://www.pantsbuild.org/docs/installation) for details.

However, we need two things to get started

* Generate pants config file pants.toml
  ```commandline
  printf '[GLOBAL]\npants_version = "2.8.1rc0"\n' > pants.toml
  ```
  
* pants script which will bootstrap a local pants installation and be the entryway for all pants actions in the repo
  * during bootstrapping it installs pants in a local ven, usually in ~/.cache/pants dir

  ```commandline
  curl -L -O https://static.pantsbuild.org/setup/pants && chmod +x ./pants
  ./pants --version
  ```

  
# Repo Structure

# Pants goals

# IDE Support

Currently no plugins exist.

See official documentation [Setting up IDE](https://www.pantsbuild.org/docs/setting-up-an-ide)




# 3wille/Dotfiles

These are my personal dotfiles.

This repository uses thoughtbot's [rcm](https://github.com/thoughtbot/rcm) with a tag-directory per
OS. Syncs between the different OS-specific versions of the dotfiles are done manually.

Currently there are files used on my Arch-Linux Thinkpad and those used on my MacBook Pro. The ``arch`` tag should work on other linux ditributions, too.

## Apply
Choose one:

```
rcup -t OSX
rcup -t arch
```

## Installation
1. See rcm.
2. Install [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
3. Install [Powerline fonts](https://powerline.readthedocs.io/en/latest/installation.html)
4. Install [Powerlevel9k ZSH Theme](https://github.com/bhilburn/powerlevel9k#installation)
``git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k``
5. Install [Vundle](https://github.com/VundleVim/Vundle.vim)
``git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim``
6. Install [package-sync](https://atom.io/packages/package-sync)
7. Install [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

```
apm install package-sync
```

### OSX

1. Install [iTerm2 Themes](https://github.com/mbadolato/iTerm2-Color-Schemes)
2. Set iTerm2 config path to ``~/.config/iTerm2``
3. Go to Settings > MenuMeters to configure them


#### Keyboard Layout

To install the keyboard layout it might be necessary to manually create the directory structure in ``~/Library``.
The layout sets ä, ö, ü, ß and € on alt+[a,o,u,s,e]

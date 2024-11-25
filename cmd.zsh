alias ssn='ssh -N -L'
alias pve='ssh -N -L 8006:10.49.5.2:8006 nas'
alias ps='ps -ef | grep'
alias sude='sudoedit'
alias free='free -h'

# 查看日志
alias log='sudo journalctl'

# git相关
alias gitc='git commit -m'
alias gits='git status'
alias gita='git add *'

# systemd 相关的
alias sys='systemctl'
alias syu='systemctl --user'

# 花里胡哨的插件
alias cat='bat'   # 有了vim为啥还有用这东西？
alias ls='eza'
alias ll='eza -l'

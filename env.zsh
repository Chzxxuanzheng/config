# sudoedit
export EDITOR="/bin/nvim"
export SUDO_EDITOR="/bin/nvim"

# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# nnn
source ~/config/nnn.sh

# ssh密钥
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/github

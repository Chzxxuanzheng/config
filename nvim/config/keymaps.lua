-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- 常量
local insert = "i"
local normally = "n"
local version = "v"

--- @param keyshout string 快捷键
--- @param match string|function 输出
--- @param desc string 描述
--- @param mod string|string[]? 状态
--- @param opt vim.keymap.set.Opts? 配置
local function map(keyshout, match, desc, mod, opt)
	if mod == nil then
		mod = normally
	end
	if opt == nil then
		opt = {}
	end
	opt["desc"] = desc
	-- if type(match) == "string" then
	vim.keymap.set(mod, keyshout, match, opt)
	-- end
end

map("<C-c>", ":", "打开cmd")
map("<C-q>", ":q<cr>", "退出")
map("<C-s>", ":w<cr>", "保存")
map("<C-z>", "u", "撤销")
map("<C-S-Z>", "<C-r>", "重做")

-- 侧边栏
map("<C-b>", ":Neotree toggle reveal<cr>", "打开侧边栏")

-- 页面操作
map("<C-w>", ":bdelete<cr>", "关闭当前页面")
map("<C-a>", ":BufferLineCyclePrev<cr>", "转到左侧")
map("<C-d>", ":BufferLineCycleNext<cr>", "转到右侧")
map("<C-S-A>", ":BufferLineMovePrev<cr>", "移动到左侧")
map("<C-S-D>", ":BufferLineMoveNext<cr>", "移动到右侧")

-- 终端
map("<C-t>", function()
	Snacks.terminal(nil, { cwd = LazyVim.root() })
end, "打开终端")

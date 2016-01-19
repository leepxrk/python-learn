apt-cache search package 搜索包

apt-cache show package 获取包的相关信息，如说明、大小、版本等

sudo apt-get install package 安装包

sudo apt-get install package - - reinstall 重新安装包

sudo apt-get -f install 修复安装"-f = ——fix-missing"

sudo apt-get remove package 删除包

sudo apt-get remove package - - purge 删除包，包括删除配置文件等

sudo apt-get update 更新源

sudo apt-get upgrade 更新已安装的包

sudo apt-get dist-upgrade 升级系统

sudo apt-get dselect-upgrade 使用 dselect 升级

apt-cache depends package 了解使用依赖

apt-cache rdepends package 是查看该包被哪些包依赖

sudo apt-get build-dep package 安装相关的编译环境

apt-get source package 下载该包的源代码

sudo apt-get clean && sudo apt-get autoclean 清理无用的包

sudo apt-get check 检查是否有损坏的依赖




第1页：安装Ubuntu Make
　　微软Build大会上搜索，一款支持Windows、Mac OS X和Linux平台的原生Visual Studio应用，名为“Visual Studio Code”让人意外，笔者之前在
　　《微软推出VS Code支持Linux和OS X平台》
　　中介绍其功能支持linux平台。近日，在itsfoss网站上针对ubuntu的web开发人员，提供实际操作来安装Visual Studio Code。（图片来源itsfoss）

　　使用Ubuntu Make来安装Visual Studio Code。据了解，Ubuntu Make是以前Ubuntu开发者工具中心，作为一个命令行工具可以帮助用户快速安装各种开发工具、语言和IDE。同时，通过Ubuntu Make轻松安装Android Studio和其他IDE，类似Eclipse。下面介绍如何使用Ubuntu Make安装VS Code。
　　安装Visual Studio Code
　　首先需要安装Ubuntu Make。Ubuntu Make存在Ubuntu 15.04资源库中，但需要Ubuntu Make 0.7以上版本才能安装Visual Studio。所以，需要通过官方PPA更新到最新的Ubuntu Make，支持Ubuntu 14.04、14.10和15.04，但仅64位版本。
　　打开终端，使用下列命令，通过官方PPA来安装Ubuntu Make：
　　sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
　　sudo apt-get update
　　sudo apt-get install ubuntu-make
　　安装Ubuntu Make完后，接着使用下列命令安装Visual Studio Code：
　　umake web visual-studio-code
　　相关下载：
　　Download Code for Linux Download Code for OS X
　　第2页：安装Visual Studio Code
　　安装过程中，将会询问安装路径，如下图：

　　经过一系列要求和条件后，询问你是否确认安装Visual Studio Code。输入“a”来确定：

　　确定之后，安装程序会开始下载并安装。安装完成后，可以发现Visual Studio Code图标已经出现在Unity启动器上。下图是Ubuntu 15.04 Unity的截图：

　　卸载Visual Studio Code，同样使用Ubuntu Make命令。如下：
　　umake web visual-studio-code remove
　　如果不使用Ubuntu Make，也可以通过微软官方下载安装文件。
Download Visual Studio Code for Linux
　　由此，很简单就可以安装Visual Studio Code，归功于Ubuntu Make，希望对用户有所帮助。

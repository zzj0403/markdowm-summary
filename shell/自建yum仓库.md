1. 配置本地系统镜像yum源

   ```
   CentOS的package移动到/opt/package
   ```

2. 直接用rpm包手动安装createrepo

   ```
   需要解决依赖关系
   python-deltarpm
   deltarpm
   createrepo
   ```

3. 生成YUM通用数据库

   ```
   createrepo /opt/package
   ```

4. 修改/etc/yum.repos.d/local-yum.repo

   ```
   vi /etc/yum.repos.d/local-yum.repo
   [loacl]
   name=local repo
   baseurl=file:////opt/package
   gpgcheck=0
   enabled=1
   ```

5. 测试

   ```
   yum clean all
   yum install lrzsz 
   ```

   



#### 停掉pid
```
kill pid_id
```
#### 查看是谁的
```
ps -o user,pid,ppid,tty,stat,lstart,cmd -p pid_id
```
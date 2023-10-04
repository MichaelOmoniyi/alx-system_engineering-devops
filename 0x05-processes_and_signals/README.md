- [ 0-what-is-my-pid ](./0-what-is-my-pid): A bash script that displays its own PID.

- [ 1-list_your_processes ](./1-list_your_processes):
    A bash script that displays a list of currently running processes
    * Must show all processes, for all users, including those which might not have a TTY
    * Display in a user-oriented format
    * Show process hierarchy

- [ 2-show_your_bash_pid ](./2-show_your_bash_pid): A Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

- [ 3-show_your_bash_pid_made_easy ](./3-show_your_bash_pid_made_easy): A Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

- [ 4-to_infinity_and_beyond ](./4-to_infinity_and_beyond):
    A Bash script that displays To infinity and beyond indefinitely.
    * In between each iteration of the loop, add a sleep 2

- [ 5-dont_stop_me_now ](./5-dont_stop_me_now):
    A Bash script that stops 4-to_infinity_and_beyond process.
    * kill must be used

- [ 6-stop_me_if_you_can ](./6-stop_me_if_you_can):
    A Bash script that stops 4-to_infinity_and_beyond process.
    * kill or killall cannot be used

- [ 7-highlander ](./7-highlander):
    A Bash script that displays:
    * To infinity and beyond indefinitely
    * With a sleep 2 in between each iteration
    * I am invincible!!! when receiving a SIGTERM signal

- [ 8-beheaded_process ](./8-beheaded_process):
    A Bash script that kills the process 7-highlander.

- [ 100-process_and_pid_file ](./100-process_and_pid_file)
    * A Bash script that:
    * Creates the file /var/run/myscript.pid containing its PID
    * Displays To infinity and beyond indefinitely
    * Displays I hate the kill command when receiving a SIGTERM signal
    * Displays Y U no love me?! when receiving a SIGINT signal
    * Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

- [ 101-manage_my_process ](./101-manage_my_process):
    Manages manage_my_process
    - When passing the argument start:
        * Starts manage_my_process
        * Creates a file containing its PID in /var/run/my_process.pid
        * Displays manage_my_process started
    - When passing the argument stop:
        * Stops manage_my_process
        * Deletes the file /var/run/my_process.pid
        * Displays manage_my_process stopped
    - When passing the argument restart:
        * Stops manage_my_process
        * Deletes the file /var/run/my_process.pid
        * Starts manage_my_process
        * Creates a file containing its PID in /var/run/my_process.pid
        * Displays manage_my_process restarted
    - Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed

- [ 102-zombie.c ](./102-zombie.c):
    A C program that creates 5 zombie processes.
    * For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
    * Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
    * When your code is done creating the parent process and the zombies, use the function bellow

- [ template.sh ](./template.sh):
    This bash script creates a boiler plate/template for the ruby scripts to prevent constant writing of the same thing.
    - To use:
    ```bash
    ./template.sh FILENAME
    ```

- [ executable.sh ](./executable.sh):
    This bash script makes files taken as its first argument executable.
    - To use:
    ```bash
    ./executable.sh FILENAME
    ```

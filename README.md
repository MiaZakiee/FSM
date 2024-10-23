# Email address validator using Finite State Machine #
**By Nino Cabiltes BSCS 3 for CS 313 Automata Theory and Formal Languages**

I have created a simple email address validator limited to top level domains (i.e com,net,gov,mil,edu,int,org) using finite state machines. The reason 2 ka FSM kay ma mess up ang domain ending tungod sa isalpha() pero in reality, I could've added a simple condition pero I was tired hehe. So what I did was split it into two wherein the first part validates everything up until the domain ending. While the second fsm validates the domain ending where I do not use the isalpha function.

### The best way to validate an email address is to send an email to said address and to get a confirmation code 🗣️🗣️🗣️ ###

References

Valid email address formats

https://snov.io/knowledgebase/what-is-a-valid-email-address-format/

Top level domains

https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains



### State Diagrams ###
![Untitled-2024-10-20-1622](https://github.com/user-attachments/assets/2b39c1a6-f308-45d1-b88e-08fab63227d8)
![image](https://github.com/user-attachments/assets/3f853333-f093-412b-bac2-ca497796db1f)

### Transition Tables ###
![image](https://github.com/user-attachments/assets/55b9e2cd-420f-4e31-8fb4-0428b729b0a7)
![image](https://github.com/user-attachments/assets/e4bb6308-31eb-4aaf-bdba-6cce93bac55a)


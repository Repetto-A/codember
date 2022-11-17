import re

data = '''
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com
usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com

usr:@itziar age:19
loc:isle psw:aaa fll:222
eme:itzi@gmail.com

usr:@midudev eme:mi@gmail.com psw:123456 age:38 loc:bcn fll:82

fll:111 eme:yrfa@gmail.com usr:@codember
psw:123456 age:21 loc:World

usr:@giroz age:22 src:12 icon:avatar.png terminal:yes
pages:server
pages:blog
blog:about
loc:tierra psw:aaa fll:222
eme:giroz@gmail.com

psw:11133 loc:Canary
fll:333 usr:@pheralb
eme:pheralb@gmail.com
'''

data = data.split('''

''')

filtered_users = []

for user in data:
    if re.search('eme:', user) and re.search('psw:', user) and re.search('age:', user) and re.search('loc:', user) and re.search('fll:', user) and re.search('usr:',user):
        filtered_users.append(user)
        
length = len(filtered_users)
user = (filtered_users[length-1]).split('usr:')
user = (user[1].split(' ')[0])

print(f'{length}{user}')
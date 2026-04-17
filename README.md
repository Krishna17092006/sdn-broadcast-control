Broadcast Traffic Control using SDN (Mininet + POX)

Broadcast Traffic Control using SDN

Name: Krishna Keerthan Reddy DR
USN / Roll No: PES1UG24CS237
Course: COMPUTER NETWORKS
📌 Objective
To control excessive broadcast traffic in a network using Software Defined Networking (SDN) by detecting broadcast packets and limiting unnecessary flooding.
________________________________________
🧠 Concept
In traditional networks, broadcast traffic is flooded to all devices, causing congestion.
Using SDN, the controller can intelligently detect broadcast packets and control their flow.
________________________________________
🛠 Tools Used
•	Ubuntu (VirtualBox)
•	Mininet (Network Emulator)
•	POX Controller (SDN Controller)
•	Python
________________________________________
⚙️ Implementation Steps
Step 1: Install Mininet
sudo apt update
sudo apt install mininet -y
Step 2: Install POX Controller
git clone https://github.com/noxrepo/pox
cd pox
________________________________________
Step 3: Create Custom Controller
File: broadcast_control.py
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    # Detect broadcast packets
    if packet.dst.is_broadcast:
        log.info("Broadcast detected - limiting traffic")
        return

    # Normal forwarding
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
________________________________________
Step 4: Run Controller
cd ~/Desktop/pox/ext
python3 ../pox.py broadcast_control
________________________________________
Step 5: Run Mininet
sudo mn --topo single,4 --controller remote
________________________________________
Step 6: Test Network
pingall
________________________________________
Step 7: Test Broadcast Control
h1 ping -b 10.0.0.255
________________________________________
📊 Results
•	Normal communication works successfully (0% packet loss)
•	Broadcast packets are detected by controller
•	Broadcast traffic is blocked
•	Network congestion is reduced
•	The system was tested using Mininet. The controller successfully detected broadcast packets and prevented flooding. The behavior was validated using ping and broadcast testing.
________________________________________
📸 Screenshots
Fig 1: Mininet pingall output

 
Fig 2: POX controller running

 
Fig 3: Broadcast ping command
 

 
Fig 4: Broadcast blocked result
 

________________________________________
✅ Conclusion
The project successfully demonstrates how SDN can be used to control broadcast traffic. The controller detects and prevents unnecessary broadcast flooding, improving network efficiency.
________________________________________
🚀 Future Scope
•	Dynamic rate limiting
•	Broadcast storm detection
•	AI-based traffic control



This demonstrates the advantage of SDN in providing centralized control over network traffic.

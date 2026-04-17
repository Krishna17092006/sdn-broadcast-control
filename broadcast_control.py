from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    # Check if packet is broadcast
    if packet.dst.is_broadcast:
        log.info("Broadcast detected - limiting traffic")
        return

    # Forward normal packets
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    log.info("Broadcast Control SDN Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

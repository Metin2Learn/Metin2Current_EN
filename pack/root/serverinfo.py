SERVER_NAME = "Server"
SERVER_IP  	= "43.242.204.112"
CH_NAME    	= "CH1"
PORT_1 		= 30003

AUTH1		= 30001
PORT_MARK	= 30003

STATE_NONE = "..."
					
STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

SERVER01_CHANNEL_DICT = {
	1:{"key":11,"name":CH_NAME,"ip":SERVER_IP,"tcp_port":PORT_1,"udp_port":PORT_1,"state":STATE_NONE,},

}

REGION_NAME_DICT = {
	0 : "",		
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SERVER_IP, "port":AUTH1, },

	}		
}

REGION_DICT = {
	0 : {
		1 : { "name" :SERVER_NAME, "channel" : SERVER01_CHANNEL_DICT, },						
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SERVER_IP, "tcp_port" : PORT_MARK, "mark" : "10.tga", "symbol_path" : "10", },
}
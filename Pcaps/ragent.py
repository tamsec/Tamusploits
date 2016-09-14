import dpkt, base64, re
dest = open('useragent', 'wb')
f = open('test.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)
for ts, buf in pcap:
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	tcp = ip.data
	if tcp.dport == 80 and len(tcp.data) > 0:
		http = dpkt.http.Request(tcp.data)
		m = re.match(r'sctf-app/(.*)/', http.headers['user-agent'])
		dest.write(base64.b64decode(m.group(1)))
		print http.headers['range']
		if http.headers['range'] == "bytes=4589-4606":
			break
dest.close()
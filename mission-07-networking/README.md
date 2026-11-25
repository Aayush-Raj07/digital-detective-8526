# Mission 7 — How Computers Communicate

## 1. Task / objective

Explain core computer networking types and concepts, test live network connectivity and DNS resolution from Terminal, and describe step-by-step how a browser opens a website.

## 2. Work completed

- Created a network concepts table explaining LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, and Client-server with everyday examples.
- Ran `ping -c 4 example.com` to test network connectivity and round-trip time.
- Ran `nslookup example.com` to inspect DNS resolution for a public domain.
- Wrote a six-step explanation of how a browser loads a website.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `ping -c 4 example.com` | Send 4 ICMP echo requests to check reachability, packet loss, and round-trip latency |
| `nslookup example.com` | Query a DNS server to find the IP addresses linked to `example.com` |

## 4. My understanding

### Task 7.1 — Network concepts

| Concept | Explanation in my own words | Example |
|---------|-----------------------------|---------|
| **LAN** | Local Area Network: connects devices over a small area such as a home, classroom, or office. | A home Wi-Fi network connecting a laptop, phone, and printer. |
| **MAN** | Metropolitan Area Network: connects multiple LANs across a city or large university campus. | A college campus network linking engineering blocks, the library, and hostels. |
| **WAN** | Wide Area Network: spans large geographical distances across cities, countries, or continents. | The global Internet connecting networks worldwide. |
| **DNS** | Domain Name System: translates human-readable website names into numeric IP addresses. | Turning `example.com` into `104.20.23.154`. |
| **Router** | A device that connects different networks and forwards data packets toward their destination. | A home Wi-Fi router sending web requests from your laptop to your ISP's network. |
| **Protocol** | An agreed set of rules that devices follow so they can format, send, and understand data. | HTTPS for loading web pages; TCP/IP for breaking and routing packets. |
| **Packet switching** | A method where data is split into small packets that travel across the network independently and are reassembled at the destination. | A webpage split into IP packets taking the best available paths across routers. |
| **Client-server** | A communication model where a client requests a service or resource and a server provides it. | A web browser (client) requesting a page from a web server (server). |

---

### Task 7.2 — Network observations

**Connectivity test (`ping -c 4 example.com`):**

```text
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=5.151 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=13.282 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=6.236 ms
64 bytes from 104.20.23.154: icmp_seq=3 ttl=58 time=10.296 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.151/8.741/13.282/3.248 ms
```

- **What a connectivity test checks:** `ping` tests whether my computer can reach a remote host over the network. It confirms the host is reachable, shows `0.0% packet loss` (all 4 packets came back), and measures round-trip time (average `8.741 ms`). The `ttl=58` value shows the packet's remaining Time To Live (hop limit) when it arrived, though the exact number of routers crossed cannot be calculated from `58` alone without knowing the remote server's starting TTL.

**DNS lookup (`nslookup example.com`):**

```text
Server:		1.1.1.1
Address:	1.1.1.1#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

- **What a DNS lookup displays:** It shows which DNS resolver answered (`1.1.1.1` on port `53`), the queried domain (`example.com`), and the public IPv4 addresses returned (`104.20.23.154` and `172.66.147.243`). Returning two addresses lets traffic be shared across multiple servers. "Non-authoritative answer" means the reply came from a recursive resolver rather than directly from the domain's authoritative nameserver.
- **Role of DNS in a browser:** People remember names like `example.com`, while routers forward packets using numeric IP addresses. When I type a website name, the browser relies on DNS to look up the IP address so it knows where to connect.

---

### Task 7.3 — What happens when opening a website?

1. **Browser (client) starts the request:** I type `https://example.com` into my browser, which acts as the **client**. The browser identifies the **protocol** (`https`) and the domain name (`example.com`).
2. **DNS lookup:** The client asks the **DNS** resolver to translate `example.com` into a numeric IP address (`104.20.23.154`).
3. **Router and network forwarding:** The client splits its connection data into packets addressed to `104.20.23.154` and sends them to the local **router**, which forwards them across ISP and internet networks using packet switching.
4. **Connecting to the server:** The packets reach the destination web **server**, where the client and server establish a TCP connection and complete a TLS handshake for encrypted HTTPS communication.
5. **Client-server protocol request:** Following the HTTP/HTTPS **protocol**, the client sends a request (such as `GET /`) asking the server for the webpage.
6. **Server response and display:** The **server** sends back an HTTP response (such as `200 OK`) along with the HTML and assets in packets. The client browser reassembles the packets and displays the webpage on screen.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-07-networking/README.md` — network concepts table, `ping` and `nslookup` outputs, and website-loading steps

## 8. Commit details

Commit message: `Explain networking concepts and website communication`
Branch: `main`
Pushed to: `https://github.com/Aayush-Raj07/digital-detective-8526`

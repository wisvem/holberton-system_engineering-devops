# 0x10. HTTPS SSL

### [0. World wide web](./0-world_wide_web)
- Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

### [1. HAproxy SSL termination](./1-haproxy_ssl_termination)
- “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

### [3. No loophole in your website traffic](./100-redirect_http_to_https)
- A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

## Contributors
[@wisvem](https://github.com/wisvem) - Wiston Venera Macías

# BetterAPI

## An great and usable api :]

# 〒▽〒 The code comments and the responses are in PT-BR 🇧🇷 Sorry if you can't understand it

### 1. **Home Endpoint**
   - **Route**: `GET /`
   - **Function**: Returns a JSON response with a message indicating available routes and a Discord link.

### 2. **IP Information Endpoint**
   - **Route**: `GET /ip/<ip>`
   - **Function**: Retrieves geolocation data for the given IP address using the `ipgeolocation.io` API and returns the data as JSON. A request log is also sent to a Discord webhook.

### 3. **Instagram User Data Endpoint**
   - **Route**: `GET /instagram/<username>`
   - **Function**: Fetches public data about an Instagram user by their username using Instagram's API. Returns filtered data (e.g., biography, followers count, following count) as JSON. The response is also sent to a Discord webhook.

### 4. **CNPJ Information Endpoint**
   - **Route**: `GET /cnpj/<cnpj>`
   - **Function**: Retrieves company information associated with the given CNPJ (Brazilian company identifier) using the ReceitaWS API and returns the data as JSON. A request log is also sent to a Discord webhook.

### 5. **Minecraft Server Status Endpoint**
   - **Route**: `GET /minecraft/<ip>`
   - **Function**: Fetches the status of a Minecraft server given its IP address using the `mcsrvstat.us` API. Returns server information (e.g., IP, port, hostname, MOTD, players online) as JSON. A request log is sent to a Discord webhook.

### 7. **Discord Boost Information Endpoint**
   - **Route**: `GET /user/<user_id>`
   - **Function**: Retrieves detailed information about a user's Discord boost status using Discord's API, including the next boost date and level. The response is returned as JSON and also sent to a Discord webhook.

### 8. **GPT-4 Response Endpoint**
   - **Route**: `GET /gpt-4/<prompt>`
   - **Function**: Sends a prompt to GPT-4 via a custom client and returns the generated response. The response is also sent to a Discord webhook.

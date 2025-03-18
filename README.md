# CodePlay Live - Shared Code Editor

A live HTML, CSS, and JavaScript code editor that you can share with friends. This application lets you write code and see the results in real-time, and easily share your creations with others via a URL.

## Features

- Live preview of HTML, CSS, and JavaScript code
- Real-time code updating
- Share your code via URL
- Save code to local storage
- Responsive design for desktop and mobile

## Installation and Setup

### Prerequisites

- [Node.js](https://nodejs.org/) (version 14 or higher)
- npm (comes with Node.js)

### Installation Steps

1. Clone or download this repository

2. Navigate to the project directory in your terminal

3. Install the required dependencies:
   ```
   npm install
   ```

4. Start the server:
   ```
   npm start
   ```

5. Open your browser and go to:
   - Local: http://localhost:3000
   - Network: http://YOUR_IP_ADDRESS:3000 (this will be displayed in the terminal)

## Sharing with Friends

Once your server is running, you can share your code editor with friends by:

1. Giving them your network URL (shown in the terminal when you start the server)
2. Using the "Share" button in the app to generate a link that includes your current code

Your friends will need to be on the same network as you to access the app via your IP address. If you want to make it accessible from anywhere, you'll need to deploy it to a hosting service or set up port forwarding on your router (advanced).

## Customization

You can customize the server by:

1. Changing the port number in the `server.js` file (default is 3000)
2. Modifying the HTML content in the `server.js` file to change the appearance or functionality

## Troubleshooting

- If the server won't start, make sure nothing else is using port 3000
- If friends can't connect, ensure they're on the same network and that your firewall allows connections on port 3000

## License

- This project is owned by Nithish.K 
- My GitHub profile = https://github.com/Shadowinfinitywarrior
- E-mail = nithishkathiravan123@gmail.com

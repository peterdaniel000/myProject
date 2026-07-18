const express = require("express");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config();

const app = express();

// Middleware
app.use(express.json());

// Custom middleware (Bonus)
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
    next();
});

// Serve static HTML
app.use(express.static(path.join(__dirname, "public")));

// GET /
app.get("/", (req, res) => {
    res.send("My Week 2 API!");
});

// POST /user
app.post("/user", (req, res) => {
    const { name, email } = req.body;

    if (!name || !email) {
        return res.status(400).json({
            message: "Name and email are required."
        });
    }

    res.json({
        message: `Hello, ${name}!`
    });
});

// GET /user/:id
app.get("/user/:id", (req, res) => {
    res.send(`User ${req.params.id} profile`);
});

// Start server
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
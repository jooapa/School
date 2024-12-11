const express = require("express");
const { GoogleGenerativeAI } = require("@google/generative-ai");
const bodyParser = require("body-parser");
const path = require("path");

const crypto = require("crypto");
let encrypted = "";
const apikey = "a3996f2954ddb616a1ee90a5e9b34bc2:f65bacdba22d2a178432d3c471615ccfe901e60ecb1ee1ab8956fe287215c76b2787d6b9d195dcef686cc528607883b5";

function encrypt(text, password) {
    const algorithm = "aes-256-cbc";
    const key = crypto.scryptSync(password, "salt", 32);
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(algorithm, key, iv);
    let encrypted = cipher.update(text, "utf8", "hex");
    encrypted += cipher.final("hex");
    return iv.toString("hex") + ":" + encrypted;
}

function decrypt(encryptedText, password) {
    const algorithm = "aes-256-cbc";
    const key = crypto.scryptSync(password, "salt", 32);
    const textParts = encryptedText.split(":");
    const iv = Buffer.from(textParts.shift(), "hex");
    const encrypted = Buffer.from(textParts.join(":"), "hex");
    const decipher = crypto.createDecipheriv(algorithm, key, iv);
    let decrypted = decipher.update(encrypted, "hex", "utf8");
    decrypted += decipher.final("utf8");
    return decrypted;
}


const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public")));

app.post("/generate", async (req, res) => {
    const genAI = new GoogleGenerativeAI(encrypted);
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
    const prompt =
        "Esitä olevan Klinoff (angry birds possu), joka kertoo henkilölle nimeltä aleksi että onko numero '" + 
        req.body.prompt + 
        "' parillinen tai pariton.";
  
    try {
        const result = await model.generateContent(prompt);
        res.json({ response: result.response.text() });
    } catch (error) {
        console.error("Error generating content:", error);
        res.status(500).json({ error: "Error generating content" });
    }
});

app.post("/check-password", async (req, res) => {
    const password = req.body.prompt.toLowerCase();
    try {
        encrypted = decrypt(apikey, password)
        res.json({ response: "Oikea salasana!" });
    } catch (error) {
        res.json({ response: "Väärä salasana!" });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

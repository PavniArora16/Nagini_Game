<h1>Nagini - Hand Gesture Controlled Snake Game</h1>
<br>
<h3>Nagini is a computer vision powered Snake Game that can be controlled entirely through hand gestures. Using a webcam, the game tracks the player's hand in real-time and translates finger gestures into movement commands for the snake.
</h3>
<br>
<h3>Features</h3>
<ul>
<li>Real-time hand tracking using MediaPipe</li>
<li>Gesture-based controls</li>
<li>Dynamic snake growth</li>
<li>Apple collection and score tracking</li>
<li>Self-collision detection and game over state</li>
<li>Webcam-based gameplay with no keyboard controls required</li>
</ul>
<br>
<h3>Technologies Used</h3>
<ul>
    <li>Python</li>
    <li>OpenCV</li>
    <li>cvzone</li>
    <li>MediaPipe</li>
    <li>Numpy</li>
</ul>
<br>
<h3>Controls</h3>
<table>
    <tr>
        <th>Fingers Shown</th>
        <th>Action</th>
    </tr>
    <tr>
        <td>0 Finger</td>
        <td>Stop</td>
    </tr>
    <tr>
        <td>1 Finger</td>
        <td>Move up</td>
    </tr>
    <tr>
        <td>2 Fingers</td>
        <td>Move Right</td>
    </tr>
    <tr>
        <td>3 Fingers</td>
        <td>Move Down</td>
    </tr>
    <tr>
        <td>4 Fingers</td>
        <td>Move Left</td>
    </tr>
</table>
<br>
<h3>Installation</h3>
<p>Clone the repository:
```bash
git clone https://github.com/PavniArora16/Nagini_Game.git
cd Nagini_Game </p>
```
<br>
<h3>Install dependencies:</h3>
<p>
```bash
pip install -r requirements.txt
```</p>
<br>
<h3>Run the game:</h3>
<p>
```bash
python snake_game.py
```</p>
<br>
<h3>How It Works</h3>
<p>
The application uses MediaPipe Hands through cvzone to detect hand landmarks from a webcam feed. The number of raised fingers is counted and mapped to movement directions. The snake moves accordingly, grows when collecting apples, and the game ends if the snake collides with itself.
</p>
<br>
<h3>Future Improvements</h3>
<ul>
    <li>Difficulty levels</li>
    <li>High score system</li>
    <li>Sound effects</li>
    <li>Multiple gesture modes</li>
    <li>Web-based version using MediaPipe JavaScript</li>
</ul>


<h3>Author: Pavni Arora</h3>


Page Replacement Algorithm 

📌 Project Overview

This project is a simulation tool that demonstrates how different page replacement algorithms work in operating systems. It allows users to input a page reference string and number of frames, then observes how pages are loaded, replaced, and managed based on algorithmic behavior.

The goal of the project is to integrate Computer Architecture concepts with Software Engineering practices, including structured programming, documentation, and Git-based collaboration.

🧠 Implemented Algorithms

The simulator supports the following replacement strategies:

✔ FIFO (First-In First-Out)

Replaces the oldest loaded page in memory.

✔ LRU (Least Recently Used)

Replaces the page that has not been used for the longest time.

✔ LFU (Least Frequently Used)

Replaces the page that has been used the least number of times.

🛠️ Features

Accepts user input for page reference strings

Simulates page hits and page faults

Displays step-by-step memory states

Calculates total page faults

Includes algorithm descriptions, pseudocode, and flow diagrams

Designed using Python

Version-controlled using Git & GitHub branches

📥 Input Format

Page reference string (space-separated integers)

Number of frames

Example:

Pages: 7 0 1 2 0 3 0 4  
Frames: 3

📤 Output

Memory state after each page request

Page fault count

Victim page replaced (if any)

Algorithm-wise comparison

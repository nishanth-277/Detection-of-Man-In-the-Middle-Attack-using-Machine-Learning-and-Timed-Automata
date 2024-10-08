
# Man in the Middle Attack Detection Using Timed Automata and Machine Learning

## Overview
This project implements a system to detect Man in the Middle (MITM) attacks using Timed Automata and a Machine Learning model. The system consists of server-side and client-side scripts to simulate communication and detect potential attacks. The detection is enhanced using a Random Forest Classifier trained on relevant network metrics.

## Project Structure
- **`server.py`**: Contains the server-side code that listens for connections from clients, calculates network metrics (IRTT, TTOC), and uses a Timed Automaton for initial attack detection.
- **`client.py`**: Contains the client-side code that connects to the server, sends and receives messages, and uses a Timed Automaton for attack detection.
- **`mitm_attacker.py`**: Implements the MITM attack, intercepting and forwarding messages between the client and server.
- **`random_forest.py`**: Trains a Random Forest Classifier on network metrics to detect MITM attacks and provides accuracy metrics.

## Prerequisites
- Python 3.x
- Required libraries:
  - `socket`
  - `time`
  - `pickle`
  - `threading`
  - `pandas`
  - `scikit-learn`

You can install the necessary libraries using pip:

```sh
pip install pandas scikit-learn
```

## Usage

### 1. Server
To start the server, run:

```sh
python server.py
```

The server will listen on `127.0.0.1:12345` and will begin detecting MITM attacks based on timed transitions and machine learning predictions.

### 2. Client
To start the client, run:

```sh
python client.py
```

The client will connect to the server and initiate communication. It will also perform its own MITM attack detection using timed transitions.

### 3. MITM Attacker
To initiate a Man in the Middle attack, run:

```sh
python mitm_attacker.py
```

This script listens on `0.0.0.0:9999` and intercepts communication between the client and server.

### 4. Training the Machine Learning Model
To train the Random Forest Classifier on the provided dataset (`MIM-Final.csv`), run:

```sh
python random_forest.py
```

This script trains the model and outputs the accuracy on the test set.

## Authors
- **Nishanth P** - 21BCE1668
- **S A Anish Thishyaa Raagav** - 21BCE1471
- **Deepesh Sai K** - 21BCE5398

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

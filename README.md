# Simple-ATM-Controller

## Implementation
1. Insert Card
2. Enter and Verify PIN 
3. Select Account
4. See Balance
5. Deposit
6. Withdraw

## ER Diagram
![ER_diagram.png](./ER_diagram.png)

## Dependency Setup
```python
conda create -n atm python=3.7.10 -y
conda activate atm
```

## Clone and Run
Clone this repository and run `main.py`.

```python
git clone https://github.com/oikosohn/simple-atm-controller
cd simple-atm-controller
python main.py
```

## Test Input
```python
base = Bank()
base.add_account('bisa', 'A_bank_account', 1000)
base.add_account('bisa', 'B_bank_account', 2000)
base.add_card('bisa', 1234)
```
- card name is `bisa` and PIN is `1234`
- The accounts linked to `bisa` are `A_bank_account` and `B_bank_account`.


## Demonstration
- [demo.gif](./demo.gif)

![demo.gif](./demo.gif)

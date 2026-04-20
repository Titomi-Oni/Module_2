## Armstrong Number

### What is an Armstrong Number?
An Armstrong number is a number where:
- Take each digit
- Cube it (multiply 3 times)
- Add them
- If the result is the same number → Armstrong number

**Example:**
153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✔️

---

### How the Program Works

We break the number into digits and check the rule.

**Steps:**
1. Take last digit using `% 10`
2. Cube the digit
3. Add it to sum
4. Remove last digit using `// 10`
5. Repeat until number becomes 0

---

### Step-by-Step Example (153)

| Step | Number | Digit | Cube | Sum |
|------|--------|-------|------|-----|
| 1    | 153    | 3     | 27   | 27  |
| 2    | 15     | 5     | 125  | 152 |
| 3    | 1      | 1     | 1    | 153 |

Final Sum = 153 → Armstrong Number ✔️

---

### Important Concepts

- `% 10` → gives last digit  
- `// 10` → removes last digit  
- `while` loop → repeats steps  

---

### Easy Trick to Remember

**Digit → Cube → Add → Compare**
```bash
# Δείξε το git history τοπικά
git log

# Δείξε τα τοπικά  κλαδιά (branches)
git branch

# Δείξε μου όλα τα branches
git branch -a

# Δείξε όλα τα tracked ή untracked αρχεία
git status

# Πρόσθεσε όλα τα αρχεία για tracking
git add .

# Κάνε commit tracked αλλαγές και δώσε ένα μήνυμα
git commit -m "message"

# Στείλε τα commits στο remote/origin
git push

# Φέρε τις origin/remote changes
git fetch

# Ένωσε τα branches
git merge <branch_name>

# Φέρε τις πιο πρόσφατες αλλαγές
git pull

# φέρε όλα τα branch από το origin
git pull --rebase

# recreate commits history
git rebase
git push -f

# Ακύρωσε το action
git rebase --abort
git merge --abort
```

# Ρουτίνα

```bash
# MAIN
git pull

# < Δουλειά >
git checkout -b <branch_name>

# < Δουλειά >
git add .
git commit -m "Type your message here"
git push

# Έτοιμος να ενώσω με το MAIN branch
git rebase -i origin/main
git push -f
```

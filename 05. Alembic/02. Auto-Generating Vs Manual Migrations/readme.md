# Auto-generating vs Manual Migrations in Alembic

Alembic provides two main methods for creating database migration scripts: **auto-generating** and **manual migrations**. Each approach has its use cases, advantages, and caveats.

---

## 🔧 Auto-generating Migrations

Auto-generation analyzes differences between your SQLAlchemy models and the current database schema, then generates migration scripts accordingly.

### ✅ Advantages

- Faster and less error-prone for standard changes.
- Great for routine additions/removals of tables or columns.
- Automatically detects type changes, constraints, and indexes.

### ❌ Limitations

- Cannot detect complex operations like renaming columns or splitting tables.
- May require manual correction or enhancement.

### 🛠️ Workflow

1. Update your SQLAlchemy models.
2. Run:
   ```bash
   alembic revision --autogenerate -m "Short description"
   ```
3. Review and edit the generated file under `alembic/versions/`.
4. Apply using:
   ```bash
   alembic upgrade head
   ```

---

## ✍️ Manual Migrations

Manual migration requires you to write both `upgrade()` and `downgrade()` functions explicitly.

### ✅ Advantages

- Full control over the migration logic.
- Can handle complex or custom changes (e.g., renames, raw SQL).

### ❌ Drawbacks

- More verbose and error-prone.
- Requires good understanding of Alembic operations.

### 🛠️ Workflow

1. Create a blank migration script:
   ```bash
   alembic revision -m "Manual migration"
   ```
2. Edit the new script:

   ```python
   def upgrade():
       op.add_column('users', sa.Column('email', sa.String))

   def downgrade():
       op.drop_column('users', 'email')
   ```

3. Run the migration as usual:
   ```bash
   alembic upgrade head
   ```

---

## 🧠 When to Use Which?

| Use Case                        | Recommended Approach |
| ------------------------------- | -------------------- |
| Adding/removing columns         | Auto-generation      |
| Simple table creation           | Auto-generation      |
| Column/table renaming           | Manual               |
| Data transformations/migrations | Manual               |
| Full control required           | Manual               |

---

## 📌 Tip

Even when using auto-generation, **always review** the generated script before applying it to your database.

---

## 🔗 References

- [Alembic Autogenerate Docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
- [Alembic Operations API](https://alembic.sqlalchemy.org/en/latest/api/operations.html)

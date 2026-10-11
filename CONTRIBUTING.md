# Contributing to Awesome Arabic Claude Skills
# دليل المساهمة في مهارات كلود العربية

[English](#english) | [العربية](#arabic)

---

<a name="arabic"></a>
## دليل المساهمة (بالعربية)

مرحباً بك! يسعدنا جداً استقبال مساهماتك لإثراء المحتوى والأدوات الموجهة للمطورين وصناع المحتوى والباحثين باللغة العربية مع Claude Code وأنظمة الوكلاء الذكية.

### طرق المساهمة:
1. **إضافة مهارة مدمجة جديدة (Native Skill)** داخل مجلد `skills/`.
2. **ربط مهارة أو مستودع خارجي (External Skill)** عبر إضافته إلى ملف `sources.json`.
3. **اقتراح أداة أو مخدم MCP أو مورد عربي** في أقسام الـ README.
4. **تحسين المهارات الحالية** أو توثيقها وتصحيح الأخطاء.

---

### شروط ومعايير المهارة (`SKILL.md`):

لكل مهارة مجلد مستقل باسمها داخل `skills/<skill-name>/SKILL.md`، ويجب أن يلتزم بالمعايير التالية:

1. **الترويسة (YAML Frontmatter)**:
   ```markdown
   ---
   name: skill-name
   description: وصف موجز ودقيق بالإنجليزية لما تقوم به المهارة ومتى يتم تفعيلها. Use when [triggers].
   ---
   ```
   - **الاسم (`name`)**: أحرف إنجليزية صغيرة مع شرطات `-` فقط.
   - **الوصف (`description`)**: 
     - لا يتجاوز 1024 حرفاً.
     - مكتوب بصيغة الغائب (Third-person).
     - الجملة الأولى توضح القدرة بدقة، والجملة الثانية تحدد كلمات التفعيل: `Use when [specific triggers]`.

2. **هيكل المهارة الموصى به**:
   - `## Quick Start / البداية السريعة`: مثال عملي سريع ومباشر.
   - `## Core Guidelines & Rules / القواعد والضوابط الأساسية`: معايير العمل اللغوية أو التقنية.
   - `## Workflows / خطوات العمل`: خطوات تسلسلية قابلة للتحقق.
   - `## Examples / أمثلة`: نماذج واضحة للمدخلات والمخرجات.

3. **الفحص المحلي والمزامنة التلقائية**:
   قم بتشغيل السكربت للتحقق من سلامة المهارة وتحديث الفهرس تلقائياً:
   ```bash
   python scripts/sync_skills.py
   ```

### أفضل الممارسات:
1. **افتح Pull Request ولا تدفع مباشرة إلى `main`.** فحوصات الـ PR تكشف الأخطاء قبل نشرها.
2. **لا تعدّل `skills.json` أو جداول الـ README يدوياً.** المزامنة تعيد كتابتها.
3. **شغّل `python scripts/sync_skills.py` قبل الـ commit** ثم `python scripts/check_catalog.py`.
4. **مصدر واحد لكل مهارة.** المهارات المزامنة تُعدَّل في مستودعها الأصلي لا هنا.
5. **اقرأ أي مهارة خارجية قبل إضافتها.** ملفات `SKILL.md` والسكربتات تعمل داخل جلسات المستخدمين.

### إضافة مهارة من مستودع خارجي:
أضف عنصراً في `sources.json`. للمستودع كاملاً:
```json
{ "repo": "owner/repo" }
```
لمجلد مهارة واحد فقط:
```json
{ "repo": "owner/repo", "dir": "skills/skill-name" }
```
- `dir` ينتهي بـ `/` يعني كل المهارات تحته. و`name` يغيّر اسم المجلد هنا.
- أضف `title_ar` و`category` ليظهرا في الفهرس.
- بدون تعديل الملف: من تبويب **Actions** شغّل **Add Skill (Manual)** وأدخل المستودع والمجلد، وسيُفتح PR تلقائياً.

---

<a name="english"></a>
## Contributing Guide (English)

Thank you for contributing to **Awesome Arabic Claude Skills**! Our mission is to curate and provide high-standard Arabic skills and resources for Claude Code and AI agents.

### Ways to Contribute:
1. **Add a built-in skill**: Create a new folder under `skills/<skill-name>/` containing `SKILL.md`.
2. **Add an external skill repo**: Add the GitHub repository to `sources.json`.
3. **Submit via GitHub Issue**: Open an issue using our [Skill Submission Template](../../issues/new?template=submit_skill.yml).
4. **Improve existing skills or documentation**: Submit a PR with enhancements.

### Skill Requirements:
- Valid YAML frontmatter with `name` and `description`.
- `description` must not exceed 1024 characters and must specify exact triggers (`Use when...`).
- Run the sync script locally before opening a pull request:
  ```bash
  python scripts/sync_skills.py
  ```
- All PRs are automatically validated by GitHub Actions.

### Best Practices:
1. **Open a pull request, do not push to `main`.** PR checks catch mistakes before they ship.
2. **Never edit `skills.json` or the README tables by hand.** The sync overwrites them.
3. **Run `python scripts/sync_skills.py`, then `python scripts/check_catalog.py`, before committing.**
4. **One source of truth per skill.** Synced skills are edited in their upstream repo, not here.
5. **Read any external skill before adding it.** `SKILL.md` files and scripts run inside users' Claude sessions.

### Adding a Skill From an External Repo:
Add an entry to `sources.json`. For the whole repo:
```json
{ "repo": "owner/repo" }
```
For one skill folder only:
```json
{ "repo": "owner/repo", "dir": "skills/skill-name" }
```
- A `dir` ending in `/` means every skill under it. `name` renames the folder here.
- Set `title_ar` and `category` so they show in the catalog.
- Without editing the file: in the **Actions** tab run **Add Skill (Manual)**, enter the repo and folder, and a pull request is opened for you.

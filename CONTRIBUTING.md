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

# Web Design System

This document constrains future web changes. The site should feel like a high-quality academic course document and engineering manual.

## Visual Principles

- Professional.
- Minimal.
- Academic.
- Calm.
- Clear.
- Content-first.
- No gimmicks.

The reader should know within 5 seconds what to study next.

## Layout Rules

- Use Starlight sidebar, content column, and table of contents.
- Do not replace Starlight with a custom app shell.
- The homepage may use a simple hero and 4-6 navigation cards.
- Week overview pages should use structured cards or lists.
- Day pages should prioritize long-form reading.
- Exercises and solutions must remain separate.
- Labs must clearly state that experiments are not proofs.

## Typography Rules

- Use the system sans-serif stack.
- Keep body line length comfortable for long reading.
- Use clear heading hierarchy.
- Do not scale font size with viewport width beyond modest responsive headings.
- Do not make notes look like slides.
- Code blocks must remain readable in light and dark mode.

## Color Rules

- Use Starlight defaults as the base.
- Use one restrained blue or indigo accent.
- Manage colors through CSS variables.
- Do not scatter hard-coded colors across components.
- Light background should be near white or off-white.
- Dark background should be charcoal or near-black.

## Component Rules

- Components should be small and reusable.
- `StudyCard` is for navigation cards.
- `WeekOverview` is for a compact seven-day path.
- `DifficultyBadge` is for Basic / Medium / Challenge / Hard labels.
- `ResourceList` is for source lists.
- `ProgressPanel` is for current learning state.

Do not introduce a heavy UI library. Do not add Tailwind unless there is a clear maintenance reason.

## Dark Mode Rules

- Dark mode must preserve contrast.
- Borders should stay visible but quiet.
- Code blocks should remain readable.
- Do not use bright neon accents.

## Accessibility Rules

- Links must be descriptive.
- Do not rely only on color to convey difficulty or status.
- Keep focus states from Starlight intact.
- Avoid low-contrast muted text.
- Avoid excessive motion.

## Anti-Patterns

- Do not make the homepage a marketing page.
- Do not add random colors.
- Do not add random icons.
- Do not add complex animations.
- Do not add glassmorphism.
- Do not add large gradients.
- Do not add cartoon illustrations.
- Do not stack cards inside cards.
- Do not mix notes, exercises, and solutions into one undifferentiated page.

## Visual QA Checklist

Before finishing a web change, check:

- Homepage is not over-designed.
- Week 1 entry is obvious.
- Navigation labels match the sidebar groups.
- Day pages are comfortable for long reading.
- Problem set and solutions are separate.
- Labs say experiments are not proofs.
- Dark mode has no obvious contrast failures.
- Mobile layout is readable.
- The site still follows this design system.


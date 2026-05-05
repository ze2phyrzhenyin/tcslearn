import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  integrations: [
    starlight({
      title: 'TCS Self-Study OS',
      description: 'A rigorous self-study system for theoretical computer science.',
      customCss: ['./src/styles/custom.css'],
      social: [],
      pagefind: true,
      sidebar: [
        {
          label: 'Start',
          items: [
            { label: 'Start Here', slug: 'start-here' },
            { label: 'System Overview', slug: 'learning-system/overview' },
            { label: 'Daily Workflow', slug: 'learning-system/daily-workflow' },
            { label: 'Weekly Workflow', slug: 'learning-system/weekly-workflow' },
            { label: 'How to Use Codex', slug: 'learning-system/how-to-use-codex' },
          ],
        },
        {
          label: 'Week 1: Foundations',
          items: [
            { label: 'Overview', slug: 'week01/overview' },
            { label: 'Day 1: Logic, Sets, Functions', slug: 'week01/day01' },
            { label: 'Day 2: Induction and Invariants', slug: 'week01/day02' },
            { label: 'Day 3: Asymptotics and Recurrences', slug: 'week01/day03' },
            { label: 'Day 4: Counting and Graphs', slug: 'week01/day04' },
            { label: 'Day 5: Probability', slug: 'week01/day05' },
            { label: 'Day 6: Linear Algebra and Convexity', slug: 'week01/day06' },
            { label: 'Day 7: Models and Reductions', slug: 'week01/day07' },
          ],
        },
        {
          label: 'Exercises',
          items: [
            { label: 'Week 1 Problem Set', slug: 'exercises/week01-problem-set' },
            { label: 'Week 1 Solutions', slug: 'exercises/week01-solutions' },
          ],
        },
        {
          label: 'Labs',
          items: [
            { label: 'Overview', slug: 'labs/overview' },
            { label: 'Asymptotics', slug: 'labs/week01-asymptotics' },
            { label: 'Recurrences', slug: 'labs/week01-recurrence' },
            { label: 'Probability', slug: 'labs/week01-probability' },
            { label: 'Automata', slug: 'labs/week01-automata' },
          ],
        },
        {
          label: 'Review',
          items: [
            { label: 'Week 1 Review', slug: 'review/week01-review' },
            { label: 'Glossary', slug: 'review/glossary' },
            { label: 'Flashcards', slug: 'review/flashcards' },
            { label: 'Mistakes to Watch', slug: 'review/mistakes-to-watch' },
          ],
        },
        {
          label: 'Meta',
          items: [
            { label: 'Resources', slug: 'meta/resources' },
            { label: 'Progress', slug: 'meta/progress' },
            { label: 'Next Actions', slug: 'meta/next-actions' },
          ],
        },
      ],
    }),
  ],
});


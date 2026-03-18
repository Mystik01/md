# Design System Strategy: The Elevated Agrarian

## 1. Overview & Creative North Star
The "Creative North Star" for this design system is **The Digital Curator**. 

In an industry often dominated by cluttered, "coupon-heavy" grocery apps, we take an editorial approach. We treat local produce like high-end art and farmers like master craftsmen. This system breaks the rigid, "boxed-in" template look of traditional e-commerce through **Intentional Asymmetry** and **Organic Layering**. By using generous white space (`spacing.20`) and overlapping imagery, we create a sense of breathability and tactile luxury. The goal is to make the user feel like they are leafing through a high-end culinary magazine, not just checking off a shopping list.

## 2. Colors & Surface Philosophy
The palette is rooted in the earth, utilizing a Material 3-inspired tonal approach to ensure accessibility while maintaining a sophisticated, "un-digital" feel.

### The "No-Line" Rule
To achieve a premium, organic aesthetic, **1px solid borders are strictly prohibited for sectioning.** Structural boundaries must be defined solely through background color shifts or tonal transitions.
- **Example:** A product grid section using `surface_container_low` (#f3f5eb) sitting directly on a `surface` (#f8faf1) background.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of fine, recycled paper. Depth is created by nesting surface-container tiers (Lowest to Highest):
1. **Base Layer:** `surface` (#f8faf1).
2. **Structural Sections:** `surface_container` (#edefe6) for large content blocks.
3. **Interactive Cards:** `surface_container_lowest` (#ffffff) to create a "pop" against darker sections.

### The Glass & Gradient Rule
For floating elements (like a navigation bar or a "Quick Add" drawer), use **Glassmorphism**.
- **Specs:** `surface` color at 80% opacity with a `backdrop-blur` of 20px. This allows the vibrant imagery of fresh produce to bleed through the UI, softening the interface.
- **Signature Textures:** Apply a subtle linear gradient to Main CTAs transitioning from `primary` (#23422a) to `primary_container` (#3a5a40). This adds a "weighted" feel that flat colors lack.

## 3. Typography
We utilize a pairing of **Plus Jakarta Sans** (Display/Headlines) and **Manrope** (Body/Labels) to balance character with utility.

*   **Display & Headlines (Plus Jakarta Sans):** Used for storytelling. The generous x-height and modern geometry convey authority and trust. Use `display-lg` (3.5rem) for hero sections with tight letter-spacing (-0.02em) to create an editorial impact.
*   **Body & Titles (Manrope):** Chosen for its exceptional readability at small sizes. `body-md` (0.875rem) is the workhorse for product descriptions, ensuring the "trustworthy" aspect of the brand is supported by clarity.
*   **Hierarchy as Identity:** Always lead with a strong Headline-to-Body ratio. A `headline-lg` title should be followed by significant `spacing.6` before the `body-lg` text to ensure the layout feels intentional and unhurried.

## 4. Elevation & Depth
We eschew traditional "drop shadows" in favor of **Tonal Layering** and **Ambient Light**.

*   **The Layering Principle:** Place a `surface_container_lowest` card on a `surface_container_low` section. This creates a soft, natural "lift" without visual noise.
*   **Ambient Shadows:** When a floating effect is mandatory (e.g., a "Cart" fab), use an extra-diffused shadow: `box-shadow: 0 20px 40px rgba(25, 28, 23, 0.06)`. The shadow color is a tinted version of `on_surface` to mimic natural light.
*   **The "Ghost Border" Fallback:** If a container requires definition against a similar background, use a **Ghost Border**: `outline_variant` (#c2c8bf) at **15% opacity**. Never use 100% opaque borders.

## 5. Components

### Buttons
*   **Primary:** `primary` (#23422a) background with `on_primary` (#ffffff) text. Radius: `full`. Use `spacing.4` horizontal padding.
*   **Secondary (Terracotta):** `secondary` (#924c00) background. Reserved for "Buy Now" or "Support Farmer" actions to draw the eye with earthy warmth.
*   **Tertiary:** No background. Use `primary` text with an underline that appears on hover.

### Cards (The "Editorial Card")
*   **Construction:** Forbid divider lines. Separate the product image, title, and price using `spacing.3` and `spacing.1.5` respectively.
*   **Radius:** Always use `rounded.lg` (2rem) for product cards to reinforce the "friendly/natural" style.
*   **Interactive State:** On hover, the card should transition from `surface_container_low` to `surface_container_lowest` with a subtle `3.5rem` ambient shadow.

### Input Fields & Selectors
*   **Text Inputs:** Use `surface_container_high` (#e7e9e0) as the fill. No border. On focus, transition the background to `surface_container_lowest` and add a `2px` "Ghost Border" of `primary`.
*   **Chips:** Use `primary_fixed` (#c7ecca) for selected states and `surface_container_highest` (#e1e3da) for unselected.

### Specialized Components
*   **The "Provenance Tag":** A small label using `tertiary_fixed` (#ffdcbb) background and `on_tertiary_fixed` (#2b1700) text to highlight farm location or organic certifications.
*   **Visual Dividers:** Replace horizontal rules with `spacing.12` or `spacing.16` of empty space. If a break is needed, use a `surface_variant` (#e1e3da) block that is only `1px` high but spans only 60% of the container width, centered.

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical image placement (e.g., an image offset to the right with text overlapping the left edge by `2rem`).
*   **Do** use `primary` (#23422a) for high-contrast navigation to meet accessibility standards.
*   **Do** embrace "The Lean": Use slightly different padding on the top vs. the bottom of sections (e.g., `spacing.20` top, `spacing.24` bottom) to create a more organic, less "grid-locked" feel.

### Don't:
*   **Don't** use pure black (#000000). Always use `on_background` (#191c17) for text to maintain the "earthy" softness.
*   **Don't** use standard `1rem` rounding for everything. Mix `rounded.lg` for containers with `rounded.full` for interactive elements to create visual rhythm.
*   **Don't** use icons without context. This is a high-trust platform; icons should be accompanied by clear `label-md` text.
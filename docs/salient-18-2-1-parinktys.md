# Salient 18.2.1: options confirmed in the theme code

This is the ground-truth list of what the user's licensed **Salient 18.2.1** can build. The static SGP demo may only show things that exist here.

- **Source:** the theme code itself, not the docs or live demos.
  - Theme: `salient/` 18.2.1. Options config: `nectar/redux-framework/options-config.php`. CSS: `css/src/*` and `css/build/*`. JS: `js/src|build/*`. Also `includes/class-nectar-element-styles.php` and `css/custom.php` (dynamic CSS).
  - **Salient Core 3.1.5.** Element maps are in `includes/nectar_maps/*.php`. Row, Column and Inner Column are defined in `includes/nectar-addons.php`. Shared option groups are in `includes/class-wpbakery-param-groups.php`. Page metaboxes are in `includes/admin/page-meta.php`.
  - **Salient WPBakery 8.7.3.**
  - Not in the extracted set: the Salient Portfolio plugin, Nectar Slider, Salient Social and the other add-on plugins. Anything that depends on them is marked *(plugin)*.
- **How it was read:** every `vc_map` / `vc_add_param` array and every Redux field was machine-parsed. That gives the exact admin labels, the saved values and the dependencies.
- **Notation:** `Label:value`. The label is what WPBakery shows in the admin. The value is what ends up in the shortcode or DOM attribute.
- **Replaces:** `docs/salient-elementai.md` (researched for 18.3.0). Where the two disagree, **this file wins**. Section 4 lists every difference.
- **Legal:** nothing from the theme is copied into this repo. Values are quoted for reference only.

---

## 0. The designer's TL;DR

1. **The renamed v18 elements all exist in 18.2.1.** Animated Text, Button, Legacy Button, Image, Sticky Content Sections, Text With Inline Media, Post Loop Builder, Tabs, Interactive Map and Color Change Section are all present. They were not introduced in 18.3.
2. **What 18.2.1 lacks** is a few small options from the 18.3 changelog:
   - Column animation *Fade In From Top*.
   - Column max-width *alignment*.
   - Also missing in 18.2.1 (unverified whether 18.3 adds them): sticky column alignment *Bottom*, header entrance *Zoom Out*, row *Parallax Fade*, a Leaflet dark scheme, and a Row-level flexbox (the Section and Column have one).
3. **Entrance animations run on jQuery Transit + anime.js, triggered by Waypoints.**
   - Global defaults: **easeOutCubic, 750 ms** (Theme Options). Most demos raise this to ~1300 ms.
   - Trigger line: the element's top crosses **88 %** of the viewport. Exceptions: *Reveal From X* uses 70 %; Milestone uses 98 %.
4. **The house curve is `cubic-bezier(.25,1,.33,1)`.** Salient uses it for button colour transitions (0.45 s) and as the fallback curve for mask reveals.
   - **Mask Reveal** (on the Inner Column, or as a Column background layer animation) is a CSS `clip-path` transition of **1.3 s**. Its curve is the global easing converted to easings.net values. For easeOutCubic that is **`cubic-bezier(0.33,1,0.68,1)`**.
5. **There is no site-wide custom cursor, magnetic button or scroll-progress bar.** The only cursor-like UI is element-level:
   - the Post Loop Builder "View/Read" indicator;
   - the Video Lightbox *Mouse Follow* play button;
   - the Self Hosted Video *Follow Mouse* button;
   - the Carousel/Gallery touch indicator;
   - the Animated Text *Link Mouse Indicator*;
   - the Sticky Content Section *Link Mouse Indicator*;
   - Content Trail.
6. **Smooth scroll is Lenis 1.1.13.**
   - Strength slider 1–100 (default 50), mapped to `lerp = 0.17 × (1.5 − strength/100)`.
   - It is **off on Safari, iOS and all mobile devices**.
7. **Page transitions:**
   - The *View Transitions API* setting offers **Fade / Horizontal Gradient Wipe / Vertical Reveal / Vertical Reveal Scale**. These run 1.2–1.3 s.
   - The legacy JS setting offers **Fade with loading icon / Center mask reveal / Horizontal basic swipe / Horizontal multi layer swipe**.
8. **Buttons:** use **Button** (`nectar_cta`). It has 10 types:
   - Basic
   - See Through
   - Arrow Animation
   - **Arrow Circle Animation**
   - Curved Arrow Animation
   - Underline
   - **Text Reveal Wave**
   - Text Reveal
   - Material
   - Next Section

   It also has presets: size sm/md/lg, fill Solid/Outline, shape Square/Rounded/Pill. Global roundness comes from *Button Styling* plus a *Button Roundness* slider (1–20 px, default 4).
9. **Column** gives you:
   - background colour **with a hover colour and a hover opacity**;
   - backdrop blur (0–50 px);
   - a mask shape;
   - shadows Small → Very Large;
   - radius 0–100 px;
   - a whole-column link.

   This is the Salient way to build hover cards without custom code.
10. **Sticky Content Sections** has 4 types:
    - *Sticky Media, Scrolling Content*.
    - *Sticky Scroll Pinned Sections*. Effects: None / Overlapping / Scale / Blurred Scale / Fade Scale, plus Stacked Appearance and dot navigation. The scale effects run 1 → 0.92, add a 5 px blur, and move −54 px when stacked.
    - *Horizontal Scrolling*. Effects: None / Stacking.
    - *Layered Card Reveal*.
11. **Post Loop Builder** can query any public CPT, e.g. a "Paslaugos" CPT. It gives you:
    - Grid / Carousel / **Stack** (Overlapping / Scale / Blurred Scale);
    - a **Vertical List** with *Featured Image Reveal / Featured Image Follow / Color Change / Slight Move*;
    - a *Featured Image Mouse Follow on Hover* grid style.
12. **Row-level motion is limited to:**
    - Background Layer Animation: Fade In / Zoom Out / Zoom Out Reveal / Slight Zoom Out Reveal / Zoom Out Slowly / **Clip Path Inset** (Triggered Once or **Scroll Position**);
    - Parallax (Subtle / Regular / Medium / High / Fixed);
    - Animated Gradient;
    - Mouse Based Parallax Scene (5 layers);
    - Color Change Section;
    - Sticky Row.

    **There is no row-level "column animation"** and no row mask.
13. **Scroll-linked transforms live on the Column / Inner Column** as *Scroll Position Advanced*. Start and end values for Translate X/Y, **Scale 0–3** and **Opacity 0–1**, plus a viewport trigger range. The Inner Column adds *Scroll Position + Entrance*.

---

## 1. Page-builder elements (18.2.1)

### 1.0 Full element index (admin name → shortcode)

| Category | Admin name (as shown) → `base` |
|---|---|
| Structure | Row → `vc_row` · Section → `vc_section` · Inner Row → `vc_row_inner` · Column → `vc_column` · Inner Column ("Column") → `vc_column_inner` · Global Section → `nectar_global_section` · legacy Full Width Section → `full_width_section`, One Half/One Third/… → `one_half` etc. |
| Typography | Animated Text → `split_line_heading` · Fancy Title → `nectar_animated_title` · Highlighted Text → `nectar_highlighted_text` · Text With Inline Media → `nectar_text_inline_images` · Rotating Words Title → `nectar_rotating_words_title` · Scrolling Text → `nectar_scrolling_text` · Responsive Text → `nectar_responsive_text` · Gradient Text → `nectar_gradient_text` · Centered Heading → `heading` · Morphing Outline → `morphing_outline` · Badge → `nectar_badge` · Price Typography → `nectar_price_typography` · Text Block → `vc_column_text` (WPBakery; + Max Width, Text Direction) |
| Buttons / links | Button → `nectar_cta` · Legacy Button → `nectar_btn` · Video Lightbox → `nectar_video_lightbox` |
| Lists | Fancy Unordered List → `fancy-ul` · Icon List → `nectar_icon_list` (+ List Item → `nectar_icon_list_item`) · Text With Icon → `text-with-icon` · Horizontal List Item → `nectar_horizontal_list_item` |
| Media | Image → `image_with_animation` · Cascading Images → `nectar_cascading_images` · Image With Hotspots → `nectar_image_with_hotspots` (+ Nectar Hotspot → `nectar_hotspot`) · Image Comparison → `nectar_image_comparison` · Image Gallery → `vc_gallery` (Salient-modified) · Self Hosted Video Player → `nectar_video_player_self_hosted` · Lottie Animation → `nectar_lottie` · Circle Images → `nectar_circle_images` · Content Trail → `nectar_content_trail` · Animated Shape → `nectar_animated_shape` |
| Interactive / cards | Fancy Box → `fancy_box` · Flip Box → `nectar_flip_box` · Icon → `nectar_icon` · Sticky Content Sections → `nectar_sticky_media_sections` (+ Sticky Content Section → `nectar_sticky_media_section`) · Tabs → `tabbed_section` (+ Tab → `tab`) · Toggle Panels → `toggles` (+ Section → `toggle`) · Page Submenu → `page_submenu` (+ Menu Link → `page_link`) · Interactive Map → `nectar_gmap` · Chat Thread → `nectar_chat_thread` (+ Chat Thread Bubble) · Team Member → `team_member` · Clients Display → `clients` (+ Client → `client`) |
| Data | Milestone → `milestone` · Progress Bar → `bar` · Pie (WPBakery) → `vc_pie` · Pricing Table → `pricing_table` (+ Pricing Column) · Star Rating → `star_rating` · Food Menu Item → `nectar_food_menu_item` |
| Sliders | Carousel → `carousel` (+ Carousel Item → `item`) · Testimonial Slider → `testimonial_slider` (+ Testimonial → `testimonial`) · Testimonial (single) → `nectar_single_testimonial` |
| Posts | Post Loop Builder → `nectar_post_grid` · Blog → `nectar_blog` · Recent Posts → `recent_posts` · Category Grid → `nectar_category_grid` · WooCommerce Products → `nectar_woo_products` |
| Other | WP Custom Menu → `vc_wp_custommenu`, Widget Sidebar → `vc_widget_sidebar`. WPBakery core elements that Salient does **not** remove, e.g. Raw HTML/JS and Single Image, stay available. |

**Removed by Salient:** the WPBakery Grid/Masonry grids, TTA Tabs/Accordion/Tour, the old accordion/toggle/tabs, Separator, Images Carousel, Progress Bar (vc), Google Maps (vc), the social elements and the WP widget elements.

### 1.1 Shared option groups (reused by many elements)

| Group (tab) | Where | Options (exact) |
|---|---|---|
| **Mask** | Column + Inner Column (tab *Background*), Image (tab *Mask*) | *Enable Mask*.<br>*Mask Shape* (icons; values `circle`, `blur-gradient`, `triangle`, `parallelogram`, `circle-rect`, `rhombus`, `star`, `heptagon`, `ellipse`, `lightning`, `circle-top-left/-top-right/-bottom-left/-bottom-right`, `x-symbol`, `custom` PNG).<br>*Mask Size* Contain / Cover / Custom (scale 0–200).<br>*Mask Alignment* per device. **Not on Row.** |
| **Backdrop Filter** | Button, Badge, Icon, Inner Row (tab *Design options*) | None / **Blur 0–50 px** / Brightness / Contrast / Grayscale / Hue Rotate / Invert / Saturate / Sepia.<br>Column and Inner Column have a simpler *Backdrop Filter: None / Blur (0–50)*. |
| **Positioning** | Image, Button, Badge, Icon, Lottie, Content Trail, Animated Shape | Position Default / Relative / Absolute (desktop, tablet, phone). Top / Right / Bottom / Left per device. Translate X/Y per device. Z-index. |
| **Layout** | Column, Inner Column, Section, Carousel Item | *Layout Type* Default / **Flexbox**.<br>Flexbox: Horizontal / Vertical per device, Justify Content, Align Items, Wrap, Reverse, Gap (default 10px) per device. |
| **Height** | Row (full-height off), Section, Column, Inner Column | Height + Min Height per device (numerical, any unit). |
| **Font sizing** | Animated Text, Badge, Chat Bubble, Button… | Custom font size per device, line height, text indent per device, **Min / Max Font Size** (clamp). |
| **Color Overlay (advanced)** | Row, Column, Section, Carousel Item, Self Hosted Video | Multi-stop gradient editor. Linear (angle) or Radial (9 positions). *Opacity* and *Opacity Hover* (0–1). |

### 1.2 Row (`vc_row`)

| Group | Option: `Label:value` |
|---|---|
| Structure | **Type:** In Container:`in_container` · Full Width Background:`full_width_background` · Full Width Content:`full_width_content`<br>**Full Height Row** (checkbox). *Column Alignment:* Middle / Top / Bottom / Stretch. The Height group applies when this is off.<br>*Fullscreen Row Position:* Middle / Top / Bottom / Full Height<br>**Column Margin:** Default, 5…100px, None, Custom<br>Equal Height Columns → *Column Content Alignment:* Top / Middle / Bottom / Stretch<br>Vertically Center Columns<br>Column Direction per device (Row Reverse / Column Reverse) |
| Background | Colour. Image per device, with *Preload*. *Background Image Type:* CSS Background Image / **Image Tag**. Position (9 + Custom X/Y). Repeat. Loading (Lazy / Skip Lazy). Hide on mobile.<br>**Video Background:** YouTube URL / MP4 / WebM / OGV, *Video Preview Image*, *Video Color Overlay*, lazy load<br>**Animated Gradient:** Colour 1 + 2. *Speed* Slow:1300 / Medium:850 / Fast:250. *Color Mix* Linear / Organic<br>**Mouse Based Parallax Scene:** positioning Center / Top / Bottom, overall strength, 5 image layers with their own strength |
| Spacing & Transform | Padding / Margin per device (numerical, negative allowed).<br>**Transform:** Translate X/Y, **Scale 0–2**, **Rotate** per device. This is static, not animated. |
| Content | *Text Color:* **Dark / Light / Custom**. This drives the header colour when *Header Permanent Transparent* or *Header Inherit Row Color* is on. Opt out with *Exclude Row From Header Color Inheritance*.<br>*Text Alignment* |
| Rounded Edges | *Border Radius* 0 / 5 / 10 / 15 / 20px / Custom per corner. *Applies To:* Row Background / Inner Content / Both |
| Advanced | Z-Index. **Sticky Row** (+ on mobile). *Sticky Alignment:* Top of Window / Bottom of Window / Top of Window Below Nav Bar.<br>Position per device (Default / Static). Overflow Visible / Hidden. **Device Visibility** per device.<br>Extra Class, **Row ID** (anchor), Row Name, Disable Ken Burns BG effect, Disable row |
| Color Overlay | *Simple:* Color Overlay + Color Overlay 2, *Enable Gradient*. *Gradient Direction:* L→R, LT→RB, LB→RT, Bottom→Top, Radial. *Overlay Strength:* Light 0.3 / Medium 0.5 / Heavy 0.8 / Very Heavy 0.95 / Solid 1.<br>*Advanced:* gradient editor (see 1.1) |
| Shape Divider | 15 shapes:<br>• Curve, Fan, Curve Opacity, Mountains<br>• Curve Asym., Curve Asym. Alt<br>• Tilt, Tilt Alt, Triangle<br>• Waves, Waves Opacity, Waves Opacity 2<br>• Clouds, Speech, Straight Section<br>Colour. *Position:* Bottom / Top / Bottom + Top. Height per device. *Bring to front?* |
| **Animation** | **Background Layer Animation:**<br>• None · Fade In:`fade-in` · Zoom Out:`zoom-out`<br>• Zoom Out Reveal:`zoom-out-reveal` · Slight Zoom Out Reveal:`slight-zoom-out-reveal`<br>• Zoom Out Slowly:`zoom-out-slow` · **Clip Path Inset:`clip-path`**<br>Clip Path settings:<br>• *Animation Type:* Triggered Once / **Scroll Position**<br>• *Applies To:* Background Layer / **Entire Row**<br>• *Inset Start* and *Inset End* (T/B/L/R per device)<br>• *Roundness Start/End*<br>• *Viewport Trigger Offset* (range 0–100, default 0,50) + *Origin* (Top / Bottom of element)<br>• *Clip Path Animation Addon:* None / Fade In / Zoom Fade In<br>Other animation options:<br>• *Background Animation Delay*<br>• Disable Background Layer Animation on Mobile<br>• **Color Change Section** (checkbox)<br>• **Parallax Background Media On Scroll** → *Speed:* Subtle:`fast` · Regular:`medium_fast` · Medium:`medium` · High:`slow` · Fixed In Place:`fixed` |

- **Not on Row:** Mask, Flexbox, *Parallax Fade*, any row-level column animation, and scroll-linked transforms. Put these on the Section or the Column instead.

### 1.3 Section (`vc_section`, a wrapper around rows)

- **Type:** same 3 values as Row. Plus the Height group and the **Layout group (Flexbox)**.
- **Text Color:** Dark / Light / Custom.
- **Spacing:** padding and margin per device.
- **Background group:**
  - colour;
  - image per device (preload, image tag, position, lazy);
  - MP4/WebM video.
- **Color Change Section.**
- **Color Overlay:** advanced gradient.
- **Rounded Edges:** radius, applies to Background / Inner Content / Both.
- **Section ID.**
- **Parallax Background Media On Scroll**, with ***Scroll Effect: Parallax / Parallax Fade*** (**only here**). *Speed:* Subtle / Regular / Medium / High.
- **Not on Section:** Shape dividers, Sticky, and Background Layer Animation.

### 1.4 Inner Row (`vc_row_inner`)

- Column Margin, Equal Height and Column Direction per device.
- Padding and margin.
- **Transform:** Translate X/Y, Scale, Rotate per device.
- **Position per device:** Default / Relative / **Absolute**, with offsets.
- **Minimum Width** and **Maximum Width** per device. *Flex* sizing.
- Z-Index, Overflow, Device Visibility.
- **Pointer Events:** All / None.
- **Backdrop Filter:** full list, tab *Design options*.
- WPBakery Design Options (css editor).

### 1.5 Column (`vc_column`) and Inner Column (`vc_column_inner`)

The two share most options. Where they differ, it is marked **(outer only)** or **(inner only)**.

| Group | Options |
|---|---|
| Spacing/Size | *Padding Type:* Simple (`Column Padding` 1–?% presets per device + *Padding Position*) / Advanced (T/R/B/L numerical per device).<br>**Transform** Translate X/Y per device (static). Height group. |
| Content | Layout Type Default / **Flexbox** (see 1.1).<br>*Column Element Direction* per device: Stacked Vertically / Inline Horizontal. *Element Alignment* Center / Top / Bottom.<br>*Column Element Spacing:* Default, 50/40/30/20/10/5px, None.<br>Centered Content. *Text Align* per device.<br>**Sticky Content** (outer only): *Functionality* JavaScript Powered / CSS Powered. With CSS: *Sticky Alignment* **Top / Middle** (no Bottom), *Sticky on Mobile*. |
| Background | *Background Color* + **Opacity** (1…0.1) and **Background Color Hover** + **Hover Opacity**<br>Background Image per device (outer: + Preload, Image Type). Position. **Stacking Order:** Behind / In Front of Background Color. *Scale Background Image To Column*. Loading.<br>Video BG: MP4 / WebM (outer: + OGV, preview image).<br>**Backdrop Filter:** None / Blur (0–50). **Mask group** (1.1). *Font Color.* |
| Shadow & Rounded Edges | **Box Shadow:** None / Small Depth / Medium Depth / Large Depth / Very Large Depth / Custom (shadow generator).<br>**Border Radius:** 0 / 3 / 5 / 10 / 15 / 20 / 50 / 100px / Custom per corner. |
| Link | **Column Link** URL + screen-reader text + same/new window |
| Advanced | **Maximum Width per device (outer only, no alignment option).** Position Default / Relative / Static (outer). Z-Index. Overflow Visible / Hidden. Extra Class. Legacy *Boxed Column*. |
| Color Overlay | Simple (2 colours, direction, strength) / Advanced gradient |
| Responsive Options | Width, Offset / visibility per device, *Tablet Column Width Inherits From* |
| Border | *Border Type* Simple / Advanced (per-side widths per device).<br>Simple: Border Width 0–8px, Colour, **Border Style** Solid / Dotted / Dashed / Double / Double Offset, **Enable Border Animation** (lines draw in) + delay. |
| **Animation** | **Column Animation Type**:<br>• Outer: Triggered Once When Visible:`default` · Scroll Position Animation:`parallax` · Scroll Position Advanced:`scroll_pos_advanced`<br>• Inner: Triggered Once · Scroll Position · **Scroll Position + Entrance:`entrance_and_parallax`** · Scroll Position Advanced |
| ↳ Scroll Position | *Movement:* Move Y Axis / Move X Axis. *Movement Intensity* (number). Persist Movement On Mobile. |
| ↳ Scroll Position Advanced | *Viewport Trigger Offset* (range 0–100, default 0,100). *Animation State* Start / End tabs, each with **Translate Y, Translate X, Scale (0–3, step .05), Opacity (0–1)**. Persist Animation On Mobile. |
| ↳ Entrance (Column Animation) | Fade In:`fade-in` · Fade In From Left · Fade In Right:`fade-in-from-right` · Fade In From Bottom · **Slight Fade In From Bottom** · Grow In · Zoom Out · Slight Twist · Flip In Horizontal:`flip-in` · Flip In Vertical · **Reveal From Right / Bottom / Left / Top** · **Mask Reveal:`mask-reveal` (inner only)**<br>Mask Reveal → *Direction:* Top / Right Top / Right / Right Bottom / Bottom / Left Bottom / Left / Left Top / Middle; *Shape:* Straight / Circle.<br>Also: *Disable … On Mobile*, **Delay** (ms), **Animation Offset** (%), **Column Animation Easing** (Inherit, or any jQuery easing Quad…Circ). |
| ↳ Background Layer Animation | None · Fade In · Zoom Out · **Zoom Out Far:`zoom-out-high`** · Zoom Out Reveal · Zoom Out Slowly · **Reveal Rotate From Top / Bottom / Left / Right:`ro-reveal-from-*`** · **Mask Reveal** (+ direction + shape, same lists). Available on outer and inner. |
| ↳ BG Parallax | *Background Image Parallax Scrolling*, speed: Minimum / Very Subtle / Subtle / Regular / Medium / High |

> To put a mask reveal on a whole **outer** column, either use *Background Layer Animation → Mask Reveal* (it only animates the background image or colour layer), or nest an Inner Row with an Inner Column set to *Mask Reveal*.

### 1.6 Typography elements

| Element (`base`) | Design-relevant options |
|---|---|
| **Animated Text** (`split_line_heading`) | **Text Effect**, shown as grouped icons:<br>• Word Animations: Reveal:`default`, Blur:`blur-bottom`, Fade:`fade-bottom`, Rotate:`twist-bottom`, Twist:`twist-bottom-2`<br>• Single Letter From Bottom: Reveal / Blur / Fade (`letter-reveal-bottom`, `-blur-bottom`, `-fade-bottom`)<br>• Single Letter From Top: Reveal / Blur / Fade<br>• Scroll Position: **Opacity:`scroll-opacity-reveal`**<br>• None<br>*Text Element* H1–H6 / Paragraph / Italic. **Stagger Animation.** **Fit Text to Container.** Disable on Mobile. Animation Delay, Animation Offset. **Max Width.** Content Align + Mobile Align. Font sizing group (min/max clamp).<br>Link tab: URL, **Link Mouse Indicator** (touch indicator BG/icon colour). *Functionality (Deprecated):* by available space / by each new line / Twist in entire element. |
| **Fancy Title** (`nectar_animated_title`) | Heading tag. *Title Style:* **Color Strip Reveal / Hinge Drop**. BG colour from the theme palette, text colour. |
| **Highlighted Text** (`nectar_highlighted_text`) | Italicised words get the effect. **Style:**<br>• Full Text BG Cover:`full_text`<br>• **Fancy Underline:`half_text`**<br>• Regular Underline<br>• Text Outline<br>• **Hand-Drawn Scribble:`scribble`**<br>• None<br>Colour Regular / Gradient (2 colours). Expansion Default / Closer / Closest.<br>Scribble:<br>• shapes (icons, default circle)<br>• thickness Thin / Regular / Thick<br>• **speed Slow 1.8s / Medium 1.3s / Fast 0.8s / No Animation**<br>• easing Ease In Out / Ease Out<br>Outline thickness. Underline 1–4px. Delay. Disable on mobile. Custom font size / line height. |
| **Text With Inline Media** (`nectar_text_inline_images`) | *Media Type:* Images / **Videos (up to 4 MP4)**. Images: 6 size presets.<br>**Animation Effect (images only):** None / Scroll Reveal:`scroll_fade` / **Circle Mask Reveal:`circle_reveal`** / Circle Crop:`circle_fade_in` + Stagger + Remove on mobile.<br>*Image Roundness* 0–50px. *Inherit Typography From* Body / Label / Italic / H1–H6. Media margin. Line height. |
| **Rotating Words Title** (`nectar_rotating_words_title`) | Beginning / dynamic / ending text. *Seconds Between Rotations* 1.5–9s. *Dynamic Text Font Family* H1–H6. **Element Animation:** None / Stagger Words + delay. Mobile Display Inline / Stacked. |
| **Scrolling Text** (`nectar_scrolling_text`) | *Direction* Standard / Reverse.<br>*Speed:*<br>• Slowest:`slower` (45s loop)<br>• Slower:`slowest` (30s)<br>• Slow (14s)<br>• Medium (7s)<br>• Fast (4s)<br>• Static<br>Repeats 2–8. *Divider:* None / Add Space / **Custom Symbol** (size Full / ¾ / ½, colour, **Spin on Scroll**). Space amount incl. Custom.<br>Effects: **Mask Edges**, **Move on Scroll**. *Italic Style:* Default / **Text Outline**. Outline thickness Ultra Thin → Extra Thick, applies to text only or text + divider.<br>Background tab: image, *BG Image Animation* (Fade In, Fade In From Bottom, Reveal Rotate From T/B/L/R), height, separate text colour over image. |
| Responsive Text (`nectar_responsive_text`) | Font Style (inherit H1–H6/p/i). Font sizing group incl. min/max clamp. Max width, link. |
| Gradient Text (`nectar_gradient_text`) | H1–H6. Colour Gradient 1 / 2. Horizontal / Diagonal. |
| Centered Heading (`heading`) | Legacy centred heading + subtitle |
| Morphing Outline (`morphing_outline`) | Text. Border thickness. Starting colour. Hover colour. |
| **Badge** (`nectar_badge`) | *Badge Style:* Default / **Minimal Line**. BG from the palette or custom. Padding S/M/L/None. Border (1–5px). **Radius 0–100px**. Display Block / Inline. Typography (Body / Label / Italic / H1–H6) + font sizing. **Backdrop Filter group.** Positioning. |
| Price Typography (`nectar_price_typography`) | Price amount. Before/after text with **scale 0–1×**. Font style p / H1–H6. |
| Fancy Unordered List (`fancy-ul`) | Icon: Standard Dash / Dot / Check / None / Font Icon. Colour, alignment, spacing 5–25px. **Enable Animation** + delay. *Link Hover Style:* Default / Opacity Change / **Animated Underline**. |
| Icon List (`nectar_icon_list`) | *Animate Element?* Vertical / Horizontal (1–5 columns). Icon size S/M/L. Icon Colored W/ BG / No BG. Items: Number or Icon, header, text. |
| Divider (`divider`) | Height. Line Type: No Line / Full Width / Small Line / **Vertical Line**. Thickness 1–10px. Opacity. **Animate Line** + delay. |

### 1.7 Buttons and links

| Element | Options |
|---|---|
| **Button** (`nectar_cta`) | **Type:**<br>• Basic:`basic` · See Through:`see-through`<br>• Arrow Animation:`arrow-animation` (arrow Left / Right) · **Arrow Circle Animation:`arrow-circle-animation`** (Min Icon Size 20–50, default 36px) · Curved Arrow Animation<br>• Underline (visible / *visible on hover*) · **Text Reveal Wave** · Text Reveal<br>• Material Button · **Next Section Button** (Down Arrow With Border / With BG Color [bounce] / Mouse Wheel / Minimal Arrow / Minimal Arrow Alt; icon size 0.5–2×; shadow)<br>**Preset** (`button_preset`): size **sm** (0.4em 1em / 0.75em) · **md** (0.65em 1.5em / 1em) · **lg** (0.85em 2em / 1.25em). *Style* Solid / Outline. *Roundness* Square / Rounded / Pill.<br>Display Tag span / p / H1–H6. Custom font size (min/max). **Button Roundness** (number).<br>Link: Regular / New Tab / **Open Video Lightbox** / Open Image Lightbox.<br>Colouring: BG (palette or custom) + **BG Hover**, Text + **Text Hover**, Border + **Border Hover**, Border Thickness 0–4px.<br>Alignment Left / Center / Right / **Stretch** per device. Margin, Padding, **Icon Gap 5–50**. **Backdrop Filter group.** Display per device. Icon tab (FA / Iconsmind / Steadysets / Linecons / Brands; Left / Right; for Basic, Text Reveal, Text Reveal Wave, Underline). Positioning tab. |
| Legacy Button (`nectar_btn`) | *Size:* Small / Medium / Large / Jumbo / Extra Jumbo.<br>*Style:* Regular · **Regular With Tilt** · See Through · See Through Solid On Hover · See Through Solid On Hover Alt · See Through 3D.<br>Palette colours incl. Color Gradient 1 / 2. Hover BG / text overrides. WPBakery *CSS Animation* (animate.css list). Icon incl. *Default Arrow*. |
| **Video Lightbox** (`nectar_video_lightbox`) | *Link Style:* Play Button · Play Button With text · Play Button With Image:`play_button_2` · **Play Button With Image – Mouse Follow** · Nectar Button.<br>With-text style: *Colored Button Pulse* / Button Bordered Small / Button Bordered Top.<br>Image style: *Hover Effect* Zoom BG Image / Zoom Button, shadow, radius 0–20, size Default / Larger.<br>Mouse-follow *Indicator Style:* Default / See Through Contrast / Solid Color.<br>**Parent Row BG Hover Relationship** (for Play Button, Play Button With text, Nectar Button). |

### 1.8 Media

| Element | Options |
|---|---|
| **Image** (`image_with_animation`) | Image size presets / custom.<br>**Desktop Max Width:** 100 / 110 / 125 / 150 / 165 / 175 / 200 / 225 / **250%** / 75 / 50% / None / Custom per device. Mobile Max Width.<br>**Animation Type:** Triggered on Entrance / Looped Infinitely (Rotate).<br>**Entrance:** Fade In · Fade In From Left / Right / Bottom · Grow In · **Slide Up** · Flip In Horizontal / Vertical · **Reveal Rotate From Top / Bottom / Left / Right**. Plus delay, disable on mobile, **Animation Easing** (per element).<br>**Scroll Based Animation:** Move Y / X + Movement Intensity + persist on mobile.<br>**Hover Animation:** None / Zoom In / **Zoom In Crop** / Color Overlay (+ colour).<br>Alignment. Link: large-image lightbox (+ caption) / URL / target incl. Lightbox.<br>Border Radius 0–20 / Custom. **Box Shadow** presets / Custom, *Shadow Method* Box Shadow / **Filter Drop Shadow**.<br>Image Loading. **Fit to Container** + object position (9). Overflow.<br>**Mask tab** + **Positioning tab.** |
| **Cascading Images** (`nectar_cascading_images`) | 4 layers, each with: image / BG colour, offset X/Y (±), rotate ±0–20° (2.5° steps), scale, **CSS Animation** (Fade In, From L / R / Bottom, Grow In, **Grow In Reveal**, Flip In, None), padding, shadow Small → Very Large, max width 100–200% desktop / mobile, mobile width.<br>Element sizing Default / **Forced Aspect Ratio** (1:1, 4:3, 3:2, 16:9, 4:5). *Time Between Animations.* Layer radius 0–20.<br>**Enable Parallax Scrolling** (per layer) + intensity Subtle / Medium / High. |
| Image With Hotspots | Hotspot icon Plus Sign / Numerical. Tooltip Show On Hover / Click / Always. Tooltip shadow. Enable Animation. Palette colour. |
| Image Comparison | Image One / Image Two only (twentytwenty). |
| Image Gallery (`vc_gallery`) | **Types:** Basic Slider / Nectar Slider Style / **Flickity Style** / Flickity Static Height / **Image Grid** / Parallax Image Grid.<br>Flickity:<br>• controls Pagination / Material Pagination / Arrows / Arrows Overlaid / Touch Indicator + Total / Touch Indicator<br>• spacing 5–70px, columns per device<br>• **Image Parallax**, **Stagger Columns**, **Subtle Image Scale When Dragging**, **Free Scroll**, **Mask Edges**<br>• Auto Play (Default / **Ticker**, speed S/M/F, pause on hover)<br>• shadows<br>Image Grid:<br>• 4 / 3 / 2 cols / Fullwidth / Constrained, masonry, spacing 1–20px<br>• *Gallery Style* (Meta on hover w/ zoom …, Meta overlaid – bottom left …)<br>• *Load In Animation* None / Fade In / Fade In From Bottom / **Perspective Fade In** |
| Self Hosted Video Player | WebM / MP4 + preview. Width 10–100%. Aspect per device (16:9, 4:3, 1:1, 2.35:1, **9:16**). *Player Functionality:* Standard / **Lightbox Trigger** (play button Default / **Follow Mouse**, hide until hovered). Hide controls, loop, autoplay (**Start When Scrolled Into View**), lazy. Radius 0–20. Shadow. Advanced gradient overlay. |
| **Lottie Animation** (`nectar_lottie`) | *Trigger:* Autoplay / Play When Visible / **Scroll Position Seek** / Hover (Play Full / **Play While Hovering-Reverse On Leave**; trigger Self / **Parent Column**). Mobile: Play / Freeze Last Frame / Remove. Loop. Trigger offset. **Start/End frames.** Speed 0–4×. Shadow. Positioning + CSS Animation tabs. |
| Circle Images | Avatar stack Overlapping / Standard, stacking order, alignment per device, Fade In, size, text, **numerical last circle** ("+12"). |
| **Content Trail** | *Type:* Images / Text (text + colour repeaters). *Animation In:* Scale / **Circle Mask** / None. *Out:* Scale / Fade / None. Aspect ratio. Radius 0–50. **Frequency 20–200px**, **Duration 0.25–2s**, **Smoothing 0–100**, random order / rotation. Overflow. Positioning + Size. |
| Animated Shape | Shape: circle / triangle / parallelogram / half-circle-top / half-circle-bottom. Entrance None / **Grow In** (+ delay, offset, easing). **Scroll Based Movement** Y / X. Positioning. |

### 1.9 Interactive, cards and data

| Element | Options |
|---|---|
| **Fancy Box** (`fancy_box`) | **Style:**<br>• Bottom Color Bar Hover Effect:`default`<br>• Color Box Hover Effect<br>• Color Box Basic<br>• **Parallax Hover Effect** (3D tilt)<br>• **Description on Hover:`hover_desc`**<br>• **Image Above Text:`image_above_text_underline`** (aspect 1:1 / 16:9 / 3:2 / 4:3 / 4:5)<br>Icon (FA / Iconsmind / **Linea** / … / custom image), image, min height.<br>hover_desc settings:<br>• hover colour (accent / extra 1–3 / custom)<br>• **Overlay Opacity** + **Hover Overlay Opacity**<br>• *Disable Movement on Hover*, *Parallax Box Image*<br>• icon Top / Bottom<br>• **Background Hover Animation: Long Zoom / Short Zoom / None**<br>Parallax: content Middle / Top / Bottom, overlay colour + opacity (0.6) → hover (0.2).<br>Border Radius Default / 5 / 10 / None.<br>Entrance: Fade In, From L / R / Bottom, Grow In, Flip H / V + delay. |
| Flip Box | Front / back: BG image, colour, overlay, Dark / Light text, icon. Min height, H / V alignment. **Flip Direction:** Horizontal To Left / Right, Vertical To Bottom / Top. |
| Icon (`nectar_icon`) | Library FA / Iconsmind / **Linea (+ draw animation via Vivus, speed S/M/F)** / Steadysets / Linecons / Brands / **Pulsating Circle** / Image. **Icon Style:** Icon Only / Border Basic / **Border W/ Hover Animation** / **Soft Color Background** / Solid Color Background / Solid W/ Shadow. Border 1–5px. Palette or custom (+hover). Padding 0–50. Backdrop Filter. Positioning. |
| **Horizontal List Item** | 1–4 columns with preset width ratios (e.g. 60/40, 20/40/40, 15/35/35/15). Responsive Stacked / Multiple Columns. Per-column text element p / H2–H5. Up to 2 CTAs. Full item link.<br>**Style:** Bottom Border, Color Hover Effect:`default` / Bottom Border, No Hover Effect / Full Border. **Border Animation** (draws in). Hover colour palette / black / white. Radius (full border). Icon tab. Inherit font p / h3–h6. |
| **Sticky Content Sections** (`nectar_sticky_media_sections`) | **Type:**<br>• **Sticky Media, Scrolling Content:`default`** → content Right / Left, content spacing 20–55vh, **media width 40–75%**, **media height 50–100vh**, mobile aspect ratio.<br>• **Sticky Scroll Pinned Sections:`scroll-pinned-sections`** → **Effect** None / Overlapping (overlap amount per device, default 50) / Scale / **Blurred Scale:`scale_blur`** / Fade Scale (fade colour); **Stacked Appearance**; **Section Navigation** (dots, colour); max height per device.<br>• **Horizontal Scrolling:`horizontal-scrolling`** → Effect None / Stacking; **Section Width 25–100%** (default 75); gap.<br>• **Layered Card Reveal:`layered-card-reveal`** → card width per device, aspect (1:1…2:1, 4:5).<br>Common: Section Height 50–100vh. **Effect Enabled per device.** Subtract Navigation Height. Content Alignment Middle / Stretch / Top / Bottom. Border Radius 0–30px.<br>Child *Sticky Content Section*: Image / **Video** (loop, cover / contain, 9 alignments) / **Color**. Link + **Link Mouse Indicator** (colour, text). |
| **Tabs** (`tabbed_section`) | **Style:** Default / Material / Minimal / Minimal Alt / Minimal Flexible Width / **Toggle Button** (2 tabs) / Vertical / Vertical Material / **Vertical Sticky Scrolling**.<br>*Tab Change Animation* Fade / None.<br>Sticky Scrolling settings:<br>• *Sticky Aspect* Tab Links / Tab Content<br>• content animation **Fade / Slide Reveal / Slide Reveal Zoom**<br>• link animation Opacity Change / Animated Underline / **Text Outline Fill**<br>• nav side, width 25–60%, functionality all / active-only, spacing, tab link element p / H2–H6<br>• CTA (See Through / Arrow Animation / Underline / Text Reveal Wave)<br>Other options:<br>• Minimal styles: optional CTA<br>• Material: full-width divider line<br>• Icon size 24–36 |
| **Toggle Panels** (`toggles`) | **Style:** Default / **Animated Circle** (position L / R, size 20–60, BG colour, divider, gap 1–30) / Minimal / **Minimal Shadow** / Inline Small. Accordion + First Open / Closed. Radius 0–20. Per toggle: palette colour, typography span / H2–H6 (style only or change tag). |
| Page Submenu | Link alignment Center / Left / Right. **Sticky?** Menu BG colour (#f7f7f7). Link colour. That's all; no blur or style variants. |
| **Interactive Map** (`nectar_gmap`) | *Map Type:* Google Map / **Leaflet (Recommended)**. Zoom 0–19. *Marker Style:* Default / **Nectar Animated**. Accent / extra marker colours. Custom marker image. **Greyscale** (Google or Leaflet). **Ultra Flat Map / Dark Color Scheme / Map Extra Color: Google greyscale only.** Leaflet info windows start open. Markers as lat / long lines. |
| Chat Thread | Incoming / outgoing avatar + name. Image size 20–50. Bubble radius 0–30. *Animation:* None / Fade In / **Typing** (+ Auto Height, **Loop**). |
| Team Member | Meta Below / Meta Overlaid / Meta Overlaid alt / **Meta Overlaid, Bio Modal** / **Meta Below, Bio Modal** (image parallax, hide arrow). |
| Clients Display | 2–6 columns. *Hover Effect:* Opacity Change / **Greyscale to Color**. Logo padding. **Fade In One By One.** Turn Into Carousel (autorotate). |
| **Milestone** | Number, inherit h1–h5 font, symbol before / after (**Superscript** alignment), subject + padding. *Animation Effect:* **Count To Value** / **Motion Blur Slide In** / None. Single decimal. Delay. Font sizes. Alignment. |
| Progress Bar (`bar`) | Title, percent, palette colour (incl. gradients). |
| Pricing Table | Default / Flat Alternative. Column highlight + colour. |
| Star Rating | 1–5 in half steps + palette colour + text. |
| Testimonial Slider | **Style:** Basic / Minimal / **Multiple Visible** / Multiple Visible Minimal (+ border). Star colour. Autorotate. Controls Pagination / **Next/Prev Arrows**. Disable height animation. Radius 0–50. **Add Shadow To Active Testimonial** (custom shadow). Custom width. Font size / line height. |
| Testimonial (single) | Small Modern / **Big Bold** / Basic / Basic – Left Image. |

### 1.10 Carousel (`carousel`) and Carousel Item (`item`)

- ***Carousel Type:*** **Flickity** / **Simple Slider** / Owl Carousel / carouFredSel (the last two are legacy).
- **Flickity:**
  - *Style:* Default / **Fixed Text Content Fullwidth** (text block + CTA, content Left / Right).
  - Columns: Desktop 1–9, Small Desktop, Tablet, Phone. **Shrink Column Width By** (peek).
  - *Controls:* Pagination / Next/Prev Arrows Overlaid / **Touch Indicator and Total Visualized** / None.
    - Touch style: Border Outline Arrows / Solid Background Arrows / **Tooltip text**.
    - **Blurred BG.**
  - Control colouring. Overflow Hidden / **Visible**. Wrap Around / No Wrap. Pagination alignment.
  - Item Spacing 5–30px. **Center Carousel Columns.** Column vertical alignment. Column padding. Top/bottom margin.
  - **Subtle Item Scale When Dragging.** **Adaptive Height.** Column colour. Radius 0–20. Column border.
  - **Mask Edges.**
- **Simple Slider:**
  - Sizing: **aspect ratio** (1:1…2:1, 4:5) or **% of screen height 20–100vh**. Min height.
  - Arrow controls: Inside / **Overlapping Slider Edges**. Colours.
  - Pagination: colouring, alignment.
  - **Touch Indicator.**
  - *Transition:* Slide / **Fade**. **Parallax Images** (slide only).
  - Wrap. **Emit slide color to row background.**
- **Autorotate:** Default (speed) / **Ticker Movement** (Slow / Medium / Fast, Default / Reverse direction). Pause on hover.
- **Carousel Item:**
  - Simple Slider: BG image (9 positions), font colour, gradient overlay (strength 0.3–1), BG colour.
  - Flickity: BG image, **BG video (MP4/WebM)**, **Background Gradient Blur**, hide on mobile, custom desktop width.
  - **Layout group (Flexbox)**, link (incl. video / image lightbox), advanced colour overlay.

### 1.11 Posts

| Element | Options |
|---|---|
| **Post Loop Builder** (`nectar_post_grid`) | **Post Type:** Blog Posts / Portfolio *(plugin)* / **Custom** (any public CPT, taxonomy narrowing). Order / orderby. Pagination None / **Load More**. Lightbox, remove links.<br>**Display Type:** Grid / Carousel / **Stack**. Stack: *Animation Effect* None / Overlapping / Scale / **Blurred Scale**, disable on mobile. Carousel: Pagination / Arrows Overlaid / Touch Indicator (+ tooltip text, blurred BG), overflow, wrap.<br>Columns 1–4 (+ small desktop / tablet / phone). Spacing none…45px or 1–4vw. Item height 30–100vh (− nav height). **Sortable filters** (top center / left / right / **sidebar**). Masonry layouts (4-col: Horizontal / Vertical Staggered / Alt / Big and Small …). **Featured First Item.**<br>Images: size, lock aspect (1:1, 16:9, 3:2, 4:3, 4:5), image width / gap / side for *next to*.<br>**Post Animation:** None / Fade in from bottom / Fade in from right / **Zoom out reveal**. Stagger Default 90 / None / 100 / 150 / 400ms. Easing. **Enable Image Parallax.**<br>Heading typography h1–h4 and render tag.<br>**Mouse Indicator:** Default / See Through / Small Tooltip, text **View / Read**, blurred BG.<br>Meta: categories (Underline / Button / See Through Button; above / below / overlaid), excerpt, date, reading time, author, **custom fields**.<br>**Display Style (Item Style tab):**<br>• Content Overlaid on Featured Image (layout Top Left / Middle / Bottom Left / w/ Shadow / Corners; overlay opacity 0.3 → hover 0.4; text opacity)<br>• Content Under Featured Image (**Card Design**)<br>• Content Next to Featured Image (vertical align incl. **Sticky**)<br>• **Featured Image Mouse Follow on Hover** (align Middle / Top Left on cursor; title contrast; opacity hover)<br>• **Vertical List** → *Hover Effect* None / **Featured Image Reveal** (overlay 0.5) / **Featured Image Follow** / **Color Change** / **Slight Move**; Read More Text / Arrow; **numerical counter**<br>*Hover Effect:* BG Zoom / Slow BG Zoom / **Animated Underline** / Animated Underline Zoom / None. Border radius. |
| Blog (`nectar_blog`) | Standard (Classic / Minimal / Featured Image Left) or Masonry (Material / Classic / Classic Enhanced / Meta Overlaid / Auto Masonry Spaced). Load-in None / Fade In / From Bottom / **Perspective**. Infinite scroll. |
| Recent Posts | Default / Minimal / Title Only / Classic Enhanced (+Alt) / List Featured First Row (+Tall) / Slider / Slider Multiple Visible (+ Single / Multiple Large Featured). Hover shadow from image colour. |
| Category Grid | Content Overlaid (7 text positions, overlay 0.3 → 0.4, **Shadow on Hover**) / **Featured Image Mouse Follow**. Subtext count / custom, always / on hover. |

### 1.12 Global Sections and the mega menu

- **Global Section element:** drop a saved section into any page. It has an *Enable Display Conditions?* option.
- **Global Section locations**, set on the section itself:
  - In Navigation Top
  - **In Navigation Top Before Scrolling**
  - After Navigation
  - Before / After Page / Post Content
  - Before / After Blog Loop, Blog Archive Loop
  - Before / After Off Canvas Menu Items, **Off Canvas Menu Meta Area**
  - **Footer**, **Footer Parallax**, After Footer
  - Single-project and WooCommerce hooks
  - Menu (mega menu)
- **Theme Options → Global Sections** has two legacy selects: *After Header Navigation* and *After Page Content*.
- **Menu item options** (Appearance → Menus):
  - **Mega Menu:** width, Global Section for desktop and mobile, alignment, BG image, column width / padding / BG, hide title.
  - **Media:** image or **video**. *Media Style* Behind / Above Text. *Media Hover* Zoom In / Zoom In Slow. Colour overlay + fade-to-transparent. Height, padding, radius.
  - **CTA button** on the item.
  - **Link Button Style:**
    - Button Accent Color
    - Button Gradient Color
    - Button Gradient Color **Animated**
    - Button Bordered Accent Color
    - Button Bordered Gradient
    - Button Bordered Gradient Animated
    - Button Bordered White BG Gradient Animated
  - **Link Text Effect:** **Text Reveal Wave** / **Text Reveal**.
  - Icons or emoji, labels, and an off-canvas image.

### 1.13 Page metabox (per page)

- **Header Navigation Entrance Animation:** None / Fade In / **Fade In From Top**, with delay and easing.
- **Transparency:**
  - Disable Transparency.
  - **Force Transparency** on Navigation, colour Light / Dark.
- **Fullscreen Rows** (fullPage.js). This takes over page scrolling. Options:
  - Animation Default Scroll / **Zoom Out + Parallax** / Parallax, speed S/M/F.
  - Dot navigation Transparent / Tooltip / Tooltip Alt / None.
  - Row BG Ken Burns.
  - Footer Default / Last Row / None.
  - Disable on mobile.
- **Page Header** (legacy hero):
  - Image / Video / **HTML5 Canvas particles**.
  - **Parallax Header**, **Box Roll Header**.
  - Height or **Fullscreen**.
  - Text effect Rotate In.
  - Alignment H / V.
  - BG / overlay / font colours.

---

## 2. Theme Options (Redux), 18.2.1

`id` is the option key. Defaults are shown in brackets.

### 2.1 General Settings

- **Styling:**
  - `theme-skin` Original / Ascend / **Material** [material].
  - **`button-styling`** Default / Slightly Rounded / **Slightly Rounded W/ Shadow** [default] / Rounded / Rounded W/ Shadow.
  - **`button-styling-roundness`** slider 1–20 [4]. It applies only to the "slightly rounded" styles.
  - `column-spacing` Default / 5–70px.
  - Primary BG [#fff], Primary Text, Primary Text (Light).
  - **`animated-underline-type`** Default / Left to Right Simple / **Left to Right Fancy**. `animated-underline-thickness` [2].
  - **Body Border (Passepartout):** Fixed Vignette / Scrolling Vignette, persist on mobile, colour, size.
  - `general-link-style` Inherit Accent Color / Basic Underline.
- **Functionality:**
  - **`smooth-scroll`** [off] + **`smooth-scroll-strength`** 1–100 [50]. The admin text says "powered by Lenis … all desktop browsers, except Safari".
  - `one-page-scrolling` (animated anchor links) [on].
  - Extended Responsive: **`max_container_width` [1425]**, `ext_responsive_padding` [90px]. Mobile padding Percent [6%] or Pixels [20px].
  - **`lightbox_script`** Magnific / **fancyBox3** [fancybox] / None. Auto Lightbox Image Links.
  - **`column_animation_mobile`** Disable [default] / Enable.
  - **`column_animation_easing`** (jQuery easing list) [**easeOutCubic**]. **`column_animation_timing`** [**750**] ms.
  - Disable Parallax BGs on Mobile. Disable Video BGs on Mobile.
  - **Back To Top Button** [on] + Keep On Mobile [off].
  - Enable WPBakery AI [off].
- **CSS/Script Related:** Custom CSS Code, Custom JS (Head), Custom JS (After Body Open), Google Maps API key.
- **Performance:**
  - Delay JavaScript Execution (all / mobile devices).
  - Lazy Load Page Builder Element Images.
  - Load Google Fonts Locally.
  - Optimize Top-level Images.
  - Move jQuery to Footer.
  - Font Display Swap.
  - Remove Block Editor CSS, global Font Awesome, legacy icon CSS and WP emojis.
- **Accent Colors:**
  - `accent-color` [#3452ff], `extra-color-1` [#ff1053], `extra-color-2` [#2AC4EA], `extra-color-3` [#333333].
  - **Theme Color Gradient** [#3452ff → #ff1053] and **Gradient #2** [#2AC4EA → #32d6ff].
  - The element palette everywhere is: Accent, Extra 1–3, Color Gradient 1/2, Black, White.

### 2.2 Typography: which elements get their own font controls

- **Navigation & Page Header:** Logo, Navigation, Navigation Dropdown, Page Heading, Page Heading Subtitle, Off Canvas Navigation, Off Canvas Description.
- **General HTML elements:** Body, **H1–H6**, **Italic**, **Bold**, **Form and Category Labels** (the *Label* style that Badge / Text Inline Media can inherit).
- **Salient Elements:**
  - Nectar Button
  - Sidebar/Footer Headers
  - Nectar/Home Slider heading and caption
  - **Testimonial Slider/Blockquote**
  - Blog Single Post Content
  - Portfolio/Post Grid Filters
  - Portfolio Caption/Excerpt
  - Sub-headers & Team Member Names
  - Dropcap
  - Woo title / secondary
- **Responsive Settings:**
  - **Fluid Typography** (root `clamp()`, used by rem values).
  - *Custom Responsive Headings:* % scale per breakpoint for H1–H6, body and blockquote. Examples: H1 small desktop 75 / tablet 70 / phone 65; H2 85 / 80 / 70.
- **Spacing:** global heading bottom margin, paragraph bottom padding.

### 2.3 Header Navigation

- **Logo & General Styling:**
  - Logo height, mobile logo height, header padding.
  - Remove desktop stickiness.
  - **Header Box Shadow** Small / **Large** [default] / Large With Bottom Line / None.
  - Menu item spacing [10].
  - **Header BG Opacity** [100].
  - **`header-blur-bg`** + *type* Default / **Progressive Gradient** + *functionality* (active when not transparent / when not at top / in all states).
  - **Header Button Link Style:** Default / Scale on Hover / **Button Shadow and Scale on Hover**.
  - Header border + colour.
- **Layout & Content:**
  - **`header_format`:**
    - Default Layout
    - Centered Menu
    - Centered Menu Alt (`centered-menu-under-logo`)
    - Menu Bottom Bar (`centered-menu-bottom-bar`, with separator and alignment options)
    - Centered Logo Menu
    - Centered Logo Menu Alt
    - **Menu Left Aligned**
    - Left Header (width 275, padding 30)
  - Full Width Header Content (+ L/R padding).
  - **Header Size:** Default (Expanded to screen edges) / **Contained**. Contained width: Match Content Width / **Automatic Width**. **Header Roundness** slider [0].
  - User account button, header text / HTML, social icons.
- **Secondary Header Bar:** Standard / With Secondary Navigation Bar (text, link, mobile behaviour).
- **Transparent Header Effect:**
  - `transparent-header`, with starting logos (light and dark, retina, mobile).
  - Starting Text Color [#fff], Dark Text Color [#000].
  - **Starting Text Opacity** 0.75 (Dimmed) / 1.0.
  - **Header Permanent Transparent**, **Header Inherit Row Color**.
  - Remove border (non-Material), **Add Shadow Behind Transparent Header**.
- **Animation Effects:**
  - **`header-hover-effect`:**
    - Color Change
    - **Animated Underline** [default]
    - **Button Background** (size S/M/L; animation Fade In / Grow In)
    - **Text Reveal**
  - **Header Hide Until Needed.**
  - **Header Resize On Scroll [ON by default]** + logo shrink px.
  - Condense Header On Scroll (Menu Bottom Bar only).
- **Dropdown / Megamenu:**
  - Dropdown opacity. Hover effect BG Colour Change / Animated Underline. Arrows.
  - **Display descriptions.** Position: bottom of bar / below the item.
  - Delay. **Animation Default / Fade In Up / Fade In.**
  - **Dropdown Roundness.** Shadow Small / Large / Large Alt / None.
  - **Mega Menu Width:** Contained / Full Screen. *Megamenu Removes Transparent Header.*
- **Header Search:**
  - AJAX search Simple / Extended List.
  - Limit to post type.
  - Typography Default / Inherit Nav.
  - Font size [48], placeholder text.
- **Off Canvas Menu:**
  - **`header-slide-out-widget-area-style`:**
    - Slide Out From Side:`slide-out-from-right` [default]
    - Slide Out From Side Hover Triggered
    - **Fullscreen Cover Slide + Blur BG:`fullscreen`**
    - Fullscreen Cover Fade:`fullscreen-alt`
    - **Fullscreen Inline with Dynamic BG:`fullscreen-inline-images`** (default BG image)
    - **Fullscreen Cover Split:`fullscreen-split`**
    - Simple Dropdown:`simple`
  - Separate mobile menu. Dropdown behaviour.
  - **Icon style** Default / **Even Lines**, icon width [22]. Simplify on mobile.
  - Button position Default / Left. "Menu" label. Social. Mobile nav items. Bottom text.
  - **Overlay strength** Solid / Dark / Medium / Light.
  - Item icons / images.
  - **Icon Button Default / Circular** (+ BG / colour).
  - Custom font size desktop / mobile.
- **Mobile Header:**
  - Layout Default / **Centered Menu**.
  - Sticky on mobile [on].
  - **Mobile breakpoint slider [1000]**.
- **Color Scheme:**
  - Light / Dark / Custom.
  - Custom colours for main nav (BG #fff, font #888, hover #3452ff, button-effect colours), secondary bar, dropdown / mega menu (BG #1F1F1F, font #CCC …) and off-canvas (BG #3452ff + optional BG 2 for a gradient, close button #ff1053).

### 2.4 Footer, Page Transitions, Page Header, Forms, misc

- **Footer:**
  - Main Footer Area [off]. Columns 1 / 2 / 3 / 4 / 4-Alt.
  - Custom colours. Copyright area, line, layout (by columns / centred), text.
  - Full width.
  - **Footer Reveal Effect** + shadow None / Small / Large / Large & same colour.
  - **Link hover** Opacity/Color Change / **Animated Underline**.
  - BG image + overlay.
  - *Info notice:* "Footers can now be created using the page builder". This means a Global Section at the *Footer* location.
- **Page Transitions:**
  - **`page-transition-type`:** Simulated with JS (Legacy) [default] / **View Transitions API (Modern)**.
  - VT effect: **Fade** [default] / **Horizontal Gradient Wipe** / **Vertical Reveal Scale:`reveal-from-bottom`** / **Vertical Reveal**.
  - Legacy:
    - *Animated Page Transitions* switch.
    - Effect: Fade with loading icon / Center mask reveal / Horizontal basic swipe / Horizontal multi layer swipe.
    - Loading icon Default / **Material** (gradient colours) or a custom image (Smooth Spin).
    - BG colour 1 / 2.
    - Disable on mobile [on]. Disable fade-out on click.
- **Page Header:**
  - Auto page title header (BG / text / overlay, featured image).
  - **Load In Animation:** None / Slide Down / Slight Zoom Out / Fade In.
  - **Down Arrow Style:** Default / Scroll Animation / Animated Arrow.
- **Form Styling:**
  - Overall Form Style Inherit / **Minimal**.
  - **Fancy Select**, **Fancy Checkbox**.
  - Submit button Default / Nectar Button / Nectar Button See Through + padding.
  - Input font size [14], padding, border width 1–3px, BG / text / border / border hover colours.
- **Call To Action** (legacy global CTA strip): text, button, colours.
- **Boxed Layout**, **Home Slider** (legacy), Social Networks, Contact Map.
- **Blog / Portfolio / WooCommerce:** archive and single templates, not needed for SGP. The portfolio project styles include *Meta + 3D Parallax on hover* and *Meta below thumb w/ shadow hover*.
- **No options** for a custom cursor, scroll progress, magnetic buttons or reduced motion. The JS never reads `prefers-reduced-motion`, so the demo must add it.

---

## 3. Visual DNA: the real motion values (from the 18.2.1 CSS and JS)

Use these numbers in the static demo, so the rebuilt WordPress site feels the same.

### 3.1 Global tokens and easings

| Thing | Value |
|---|---|
| `:root` tokens | `--nectar-cubic-bezier-out: cubic-bezier(0.3,1,0.3,1)` · `--nectar-cubic-bezier-in-out: cubic-bezier(0.76,0,0.24,1)` · `--nectar-header-hover-timing: 0.65s` · `--page-color-change-section-transition-time: 0.8s` |
| Most-used curves in the theme CSS (most frequent first) | `cubic-bezier(.12,.75,.4,1)` (links, arrows, tabs) · `(.25,1,.33,1)` (button colours, text reveal) · `(.2,1,.2,1)` · `(.15,.75,.5,1)` · `(.2,.75,.5,1)` · `(.2,1,.22,1)` · `(.05,.2,.1,1)` (hover lifts, image zoom) · `(.215,.61,.355,1)` |
| Entrance engine (columns / images) | jQuery **Transit 0.9.9** + **anime.js 3.2.1**, triggered by **Waypoints** |
| Global entrance defaults | Theme Options: **easeOutCubic** + **750 ms**. JS falls back to 650 ms if there is no body attribute. Transit maps easeOutCubic to `cubic-bezier(.215,.61,.355,1)`, easeOutQuart to `(.165,.84,.44,1)`, easeOutExpo to `(.19,1,.22,1)`, easeOutQuint to `(.23,1,.32,1)`. |
| CSS-generated easings (mask reveal etc.) | These use the easings.net table: easeOutCubic `(0.33,1,0.68,1)`, easeOutQuart `(0.25,1,0.5,1)`, easeOutExpo `(0.19,1,0.22,1)`, easeInOutCubic `(0.65,0,0.35,1)`, easeInOutQuart `(0.76,0,0.24,1)` |
| Entrance trigger (Waypoint offset) | Column / Image **88 %** (top of element at 88 % of viewport height). Image *Reveal Rotate L/R* 75 %. Image *Slide Up* 99 %. Column *Reveal From X* **70 %**. Column *Mask Reveal* 88 %. Milestone **98 %** (110 % on mobile). Animated Text "bottom-in-view". All can be changed with *Animation Offset* (%). |
| Mobile | Entrances are **off below 1000 px** unless *Page Builder Element Animations On Mobile = Enable* |
| Breakpoints | Header mobile breakpoint slider [1000]. Grid: desktop ≥1000, tablet 691–999, phone ≤690. |
| Parallax factor (speed labels) | Subtle `fast` = **0.20** · Regular `medium_fast` = 0.28 · Medium 0.40 · High `slow` = 0.60 · Very Subtle 0.12 · Minimum 0.09 (column BG only) |
| Lenis | v1.1.13, `lerp = 0.17×(1.5 − strength/100)` (strength 50 → 0.17). Desktop only, never Safari. |

### 3.2 Entrance animations

| Effect | Start state → end | Timing |
|---|---|---|
| Column *Fade In From Bottom* | `translateY(100px)` → 0 (anime), opacity 0 → 1 | transform = theme duration + easing, opacity **500 ms** |
| Column *Slight Fade In From Bottom* | `translateY(50px)` | same |
| Column *Fade In From Left / Right* | `translateX(∓45px)` | theme duration |
| Column *Grow In* / *Zoom Out* | `scale(.75)` / `scale(1.2)` | theme duration |
| Column *Slight Twist* | `rotateY(20deg) rotateZ(-4deg)` | theme duration |
| Column *Flip In H / V* | `rotateY(25deg)` / `rotateX(-45deg) translateY(120px)` | theme duration |
| Column **Reveal From Bottom / Top / Left / Right** | The **inner is slid in inside an overflow-hidden column**: `translateY(±101%)` / `translateX(±120%)` → 0. This is a slide-in behind a mask, not a clip-path wipe. | theme duration + column easing, trigger 70 % |
| Inner Column **Mask Reveal** (and Column BG *Mask Reveal*) | CSS `clip-path`. **Straight**: `inset()` from the chosen side, e.g. Bottom = `inset(100% 0 0 0)` → `inset(0)`; Middle = `inset(50% 0 50% 0)`. **Circle**: `circle(0% at edge)` → `circle(125–150%)`. | **`transition: clip-path 1.3s`** + global or column easing (easings.net curve) |
| Image *Fade In From Left / Right / Bottom* | `translateX(∓20%)` / `translateY(100px)` | theme duration |
| Image *Grow In* | `scale(.75)`, opacity .6 s `cubic-bezier(.15,.84,.35,1.25)` | theme duration |
| Image / Column BG **Reveal Rotate From X** | wrapper `translate3d(±250px)` + inner `rotate(±25deg)` (counter-rotated image) → 0 | **2.3 s `cubic-bezier(.2,.65,.3,1)`** |
| **Animated Text**, word effects | Reveal `translateY(1.3em)`; **Blur** `blur(10px)` + `translateY(.25em)` + opacity 0; Fade `translateY(.5em)`; Rotate `rotateX(-70deg)` (origin −2em); Twist `rotateX(-40deg) rotateY(13deg) rotateZ(13deg)` | **1.2 s `cubic-bezier(.25,1,.5,1)`**. With *Stagger*: 500 ms / word count, clamped **15–50 ms** per word |
| Animated Text, letter effects | anime.js, same start states (blur 10px / ±.25em, ±1.3em, ±.5em) | **1200 ms `cubicBezier(.25,1,.5,1)`**, stagger 400 / letters, clamped **20–35 ms** |
| Animated Text *Scroll position Opacity* | words start at **opacity .2** and light up with scroll | scroll-linked |
| Highlighted Text | `background-size 0% → 100%` | **.9 s `cubic-bezier(.15,.75,.4,1)`**. Scribble 0.8 / 1.3 / 1.8 s |
| Milestone *Count To Value* | CountUp from 0 | **2.2 s easeOutCubic**. *Motion Blur*: digits stagger 200 ms, .65 s `cubic-bezier(0,0,.17,1)` |
| Row BG *Fade In* | opacity | .85 s ease-out |
| Row BG *Zoom Out* / *Zoom Out Slowly* | `scale(1.25)` / `scale(1.35)` → 1 | 2.5 s `cubic-bezier(.1,.55,.4,1)` / **8 s `cubic-bezier(.1,.2,.7,1)`** |
| Row BG *Zoom Out Reveal* (Slight) | wrapper `scale(.7)` (`.92`), inner `scale(1.75)` (`1.15`) | 1.3 s `cubic-bezier(.12,.75,.4,1)` |
| Row *Clip Path Inset*, Triggered Once | custom `inset(… round …)` start → end | first row: **1.3 s `cubic-bezier(.25,.1,.18,1)`**; other rows: **2 s `cubic-bezier(.6,.06,.18,1)`**. Addon Zoom: `scale(1.2)` → 1. Fade: 1.3 s. |
| Color Change Section | page BG transitions when a row crosses mid-viewport | **0.8 s** |
| Post Loop Builder *Zoom out reveal* | `clip-path: inset(5% round 10px)` style | 1.2 s `cubic-bezier(.65,0,.35,1)`. Item stagger default 90 ms. |

### 3.3 Hover and interaction effects

| Element | Value |
|---|---|
| Button, default colour change | `border-color / color / background-color .45s cubic-bezier(.25,1,.33,1)` |
| Button, *Rounded W/ Shadow* / *Slightly Rounded W/ Shadow* hover | **`translateY(-3px)` + `box-shadow: 0 20px 38px rgba(0,0,0,.16)`** |
| Button roundness | *Slightly Rounded* = slider value (default **4px**). *Rounded* = **200px** (pill). |
| **Arrow Circle Animation** | `--nectar-button-duration .55s`, `--nectar-button-easing cubic-bezier(.12,.75,.4,1)`. The circle `clip-path: circle(50%)` shrinks to `circle(45%)` on hover. The arrow exits `translate(50%,-150%)` and a second arrow enters from the bottom-left. The circle is `max(1.4em, 36px)`. |
| **Text Reveal Wave** | letters `translateY(115%)` → 0, **.5 s `cubic-bezier(.46,.4,.56,.87)`**, per-letter delay **15 ms**. BG colour .5 s `(.23,.46,.4,1)`. |
| Text Reveal (button, menu) | text slides `translateY(-100%)`, copy from `-20%`, **.55 s `cubic-bezier(.25,1,.33,1)`** |
| Arrow Animation / Underline | .45 s / .4 s `cubic-bezier(.23,.46,.4,1)` (underline `scaleX` left → right) |
| Curved Arrow Animation | .9 s `cubic-bezier(.15,.75,.5,1)` |
| Header Animated Underline | `transform .35s cubic-bezier(.52,.01,.16,1)` |
| Header Hide Until Needed | `transform .3s ease` (`translateY(-100%)`) |
| Fancy Box *Bottom Color Bar* | 6 px bar `scaleX(0 → 1)` **.45 s `cubic-bezier(.24,1,.3,1)`**. BG `scale(1.13)` .6 s same curve. |
| Fancy Box *Description on Hover* | card **`translateY(-10px)` + `box-shadow 0 25px 55px rgba(0,0,0,.22)`**, .65 s `cubic-bezier(.05,.2,.1,1)`. Hidden text from `translateY(20px)`, .65 s, delay .15 s. BG Long Zoom `scale(1.2)` over **9 s**; Short Zoom `scale(1.13)` .8 s. Gradient scrim to `rgba(15,15,15,.75)`. |
| Fancy Box *Image Above Text* | image `scale(1.1)` .75 s `cubic-bezier(.2,.75,.5,1)` + underline |
| Image hover | *Zoom In* `scale(1.13)`. *Zoom In Crop*: inner `scale(1.15)` + frame `scale(.95)`. Both .65 s `cubic-bezier(.05,.2,.1,1)`. |
| Horizontal List Item | fill flips up: `perspective(1000px) rotateX(90deg)` → 0, origin bottom, **.4 s `cubic-bezier(.2,0,.15,1)`**. Row border `rgba(0,0,0,.12)`, padding 22 px. |
| Toggles *Animated Circle* | SVG circle stroke draws (`dashoffset 115 → 0`), plus rotates, panel `max-height` — all **.85 s `cubic-bezier(.76,0,.24,1)`**. Circle 40 px, gap 15 px. |
| Toggles default | `max-height .5s ease`, title `.2s linear` |
| Tabs *Minimal* | underline 4 px, `transform .3s cubic-bezier(.12,.75,.4,1)` |
| Page Submenu | sticky `.3s`, link opacity .7 → 1 in .1 s. Default BG `#f7f7f7`. |
| Sticky Pinned *Scale / Blurred Scale / Fade Scale* | previous card `scale 1 → .92`, `blur(0 → 5px)` for Blurred, `translateY 0 → −54px` when Stacked. anime.js timeline seeked by scroll. |
| Scrolling Text | CSS `translateX(-20% → …)` loop: 45 / 30 / 14 / 7 / 4 s per cycle |
| Off-canvas *Fullscreen Cover Split* | right side `translateY(35px)` → 0, **.85 s `cubic-bezier(.2,.75,.5,1)`**, delay .3 s. Links `.37s cubic-bezier(.52,.01,.16,1)`. |
| View Transitions | *Vertical Reveal*: new page `clip-path inset(90% 0 0 0)` + `translateY(10%)` → none, old page `translateY(-10%)` + opacity .3, **1.3 s `cubic-bezier(.55,0,.1,1)`**. *Vertical Reveal Scale*: old page `scale(.93) translateY(-15%)`. *Gradient Wipe*: 1.2 s `(.45,0,.35,1)`. |

### 3.4 Shadows and radii presets

- **Shadow presets.** The same presets are used on Image, Column, Cascading, Video and Gallery.
  - *Small Depth*: `0 1px 0 rgba(0,0,0,.04), 0 2px 7px rgba(0,0,0,.05), 0 12px 22px rgba(0,0,0,.06)`.
  - *Medium*: `0 30px 80px rgba(0,0,0,.14), 0 20px 70px rgba(0,0,0,.12)` for images. Columns use `0 20px 30px rgba(0,0,0,.2)…`.
  - *Large*: `0 40px 100px rgba(0,0,0,.15), 0 25px 80px rgba(0,0,0,.1)`.
  - *Very Large*: `0 60px 135px rgba(0,0,0,.14), 0 15px 65px rgba(0,0,0,.14)`.
  - Images can use `filter: drop-shadow()` versions instead.
- **Radius presets:**
  - Column 0 / 3 / 5 / 10 / 15 / 20 / **50 / 100** / custom
  - Row 0–20 / custom
  - Image and Video 0–20 / custom
  - Carousel 0–20
  - Sticky Sections 0–30
  - Badge 0–100
  - Toggles 0–20
  - Content Trail 0–50
  - Header Roundness slider
  - Dropdown Roundness slider
- **Container:** max **1425 px**, side padding **90 px** desktop / **6 %** mobile.

---

## 4. `salient-elementai.md` (18.3 research) checked against the 18.2.1 code

### 4.1 Renamed elements: **all present in 18.2.1**

| Name in `salient-elementai.md` | 18.2.1 admin name | `base` | Status |
|---|---|---|---|
| Animated Text (ex Split Line Heading) | **Animated Text** | `split_line_heading` | exists |
| Button (ex Call to Action) | **Button** | `nectar_cta` | exists (with presets) |
| Legacy Button | **Legacy Button** | `nectar_btn` | exists |
| Image (ex Image with Animation) | **Image** | `image_with_animation` | exists |
| Sticky Content Sections | **Sticky Content Sections** / Section | `nectar_sticky_media_sections` / `_section` | exists, all 4 types |
| Text With Inline Media | **Text With Inline Media** | `nectar_text_inline_images` | exists (videos too) |
| Post Loop Builder | **Post Loop Builder** | `nectar_post_grid` | exists (incl. Stack) |
| Tabs ("Tabbed Section") | **Tabs** | `tabbed_section` | exists |
| Interactive Map | **Interactive Map** | `nectar_gmap` | exists (Leaflet) |
| Color Change Section | Row / Section checkbox *Color Change Section* | `color_change_section` | exists |
| Animated Title | shown as **Fancy Title** | `nectar_animated_title` | exists (Color Strip Reveal / Hinge Drop) |
| Section (container) | **Section** | `vc_section` | exists |
| Chat Thread, Content Trail, Price Typography, Animated Shape, Circle Images, Badge | same | — | all exist |

### 4.2 Tagged `[CL 18.3]` in the old doc, and **absent from 18.2.1**

| Item | 18.2.1 reality |
|---|---|
| Column animation **"Fade In From Top"** | Not in either Column list. Use *Reveal From Top* (slide inside a mask) or Inner Column *Mask Reveal → Top*. |
| Column **Max Width alignment** | The Column has *Maximum Width* per device (outer only) but **no alignment option**. Centre it with Column *Centered Content* / text-align, or an Inner Row with Max Width. |

### 4.3 Other claims in the old doc that the 18.2.1 code does **not** support

Do not design with these.

| Claim | 18.2.1 code |
|---|---|
| Row **Flexbox / "Bento" controls** [CL 18.0] | **Not on Row.** The *Layout Type: Flexbox* group is on **Section, Column, Inner Column and Carousel Item**. |
| Row **Parallax Fade** (`parallax_effect--parallax_fade`) | **Section only** (*Scroll Effect: Parallax / Parallax Fade*). Row speeds: Subtle / Regular / Medium / High / Fixed In Place. |
| Section **supports shape dividers** | No. Shape Divider is a **Row** tab only. |
| Column **Sticky alignment Bottom** | CSS sticky: **Top / Middle** only. JS sticky has no alignment. |
| Column entrance **Rotate Reveal** [CL 12.0] | Not a column entrance. *Reveal Rotate From T/B/L/R* exists as an **Image** entrance and as a Column **Background Layer** animation. |
| Column entrance **Mask Reveal** on any column | Entrance *Mask Reveal* is **Inner Column only**. The outer Column only has BG-layer *Mask Reveal*. |
| **Header Navigation Entrance Animation: Fade In / Zoom Out** (theme option) | It is a **per-page metabox** option with **None / Fade In / Fade In From Top**. There is no Zoom Out. |
| Text With Inline Media: **Circle Mask Reveal on MP4 clips** | *Animation Effect* (None / Scroll Reveal / Circle Mask Reveal / Circle Crop) depends on **Media Type = Images**. Video clips get **no entrance effect option**. |
| Interactive Map **Leaflet dark scheme / extra hue / Ultra Flat** | *Ultra Flat Map*, *Dark Color Scheme* and *Map Extra Color* depend on the **Google** greyscale switch. Leaflet only gets *Greyscale* + Nectar Animated markers + info windows. |
| Icon **"Circle Pulse"** | Not an option. It has *Pulsating Circle* (icon library) and *Border W/ Hover Animation* (icon style). The Vivus line-draw works **only for Linea icons**. |
| Legacy Button **Gradient / Gradient Reverse** styles, *Regular w/ arrow*, *Hover Effect shadow/scale* | Styles are Regular, **Regular With Tilt**, See Through, See Through Solid On Hover (+Alt), See Through 3D. Gradients come from the colour palette (Color Gradient 1/2). The arrow comes from Icon library *Default Arrow*. There is no hover-effect option. |
| Badge **see-through style** | Badge styles: **Default / Minimal Line** only (+ backdrop filter). |
| Fancy Box **"Movement" styles** | None. Only *Disable Movement on Hover* (Description on Hover style). |
| Carousel (Flickity) **plain "Arrows" control** | Carousel: Pagination / **Next/Prev Arrows Overlaid** / Touch Indicator and Total / None. Plain arrows exist in **Image Gallery** and **Testimonial Slider**. |
| Scrolling Text **image-filled letters** | No such option. The *Background* tab puts an image layer behind the text, with animation and *Separate Text Coloring When on top of Image*. |
| Swiper in the theme JS | **No Swiper file** is shipped in `js/*/third-party`. Nectar Slider is a separate plugin, not in this extraction. |
| "Before footer" Global Section location | Actual labels: *After Page/Post Content*, *Footer*, **Footer Parallax**, *After Footer*. |
| Tabs "per-tab CTA" | The CTA is set on the **Tabs element** (Minimal styles and Vertical Sticky Scrolling), not per tab. |

### 4.4 Present, but with different labels or details

- Highlighted Text "Half Text BG Cover" = **Fancy Underline** (`half_text`).
- Off-canvas "Fullscreen Split" = **Fullscreen Cover Split**.
- View Transitions "Vertical Reveal Scale" = value `reveal-from-bottom`.
- Legacy transition "Horizontal Swipe" = **Horizontal basic swipe** or **Horizontal multi layer swipe**.
- Column border styles also include **Dotted**.
- Row Transform also has **Rotate**.
- Full Height Row alignment is *Column Alignment: Middle / Top / Bottom / Stretch*.
- "Contained" header is **Header Size = Contained** (+ Automatic Width, Header Roundness), not a layout.
- Header hover effects also include **Button Background**.
- Smooth-scroll strength default is **50**. Signal's 60 is a demo setting.
- Timing: the theme default is **750 ms easeOutCubic**. The 1300 ms seen in demos is a Theme Options value, not a default.
- Mask Reveal uses the easings.net curve `(0.33,1,0.68,1)` for easeOutCubic, not `(0.215,0.61,0.355,1)`.

### 4.5 Present in 18.2.1 but missing from the old doc (useful extras)

- **Column / Inner Column *Scroll Position Advanced*** also animates **Opacity** (start / end 0–1). The Inner Column has *Scroll Position + Entrance*.
- **Row Clip Path Inset:** per-device start and end insets, **Roundness Start / End**, *Applies To Entire Row*, trigger origin, and an addon *Fade In / Zoom Fade In*.
- **Column BG Layer animations:** *Zoom Out Far*, *Reveal Rotate From X*, *Mask Reveal*. BG parallax speeds *Minimum / Very Subtle*.
- **Header:**
  - *Header Button Link Style* (Scale / **Shadow and Scale on Hover**).
  - Dropdown *Fade In Up*.
  - Off-canvas icon *Even Lines* / *Circular*.
  - Mobile header *Centered Menu*.
  - Progressive-gradient header blur.
- **Menu items:**
  - **Button styles**, incl. *Gradient Animated* and *Bordered White BG Gradient Animated*.
  - Link effect **Text Reveal Wave / Text Reveal**.
  - Image or video media with zoom hover.
- **Button:** *Next Section* styles (Mouse Wheel, Minimal Arrow…); link type *Open Video / Image Lightbox*.
- **Sticky Content Section** children can be **Image, Video or Color**, with a link and a *Link Mouse Indicator* (custom text).
- **Post Loop Builder:**
  - *Content Next to Featured Image* with **Sticky** text.
  - *Card Design*.
  - Vertical List **numerical counter** and Read More Arrow.
  - Masonry *Big and Small*.
  - Custom-field meta.
- **Image Gallery** load-in *Perspective Fade In*.
- **Icon** style *Soft Color Background*.
- **Toggles *Animated Circle*** (size, gap, divider, BG).
- **Page Header** load-in (*Slide Down / Slight Zoom Out / Fade In*) and down-arrow styles.
- **Form Styling *Minimal*** + fancy select / checkbox.

---

## 5. JavaScript libraries shipped with 18.2.1

From `js/build/third-party` and `nectar/helpers/enqueue-scripts.php`.

| Library (file) | Version seen | Used for |
|---|---|---|
| **Lenis** (`js/build/nectar-smooth-scroll.js`, + `css/build/plugins/lenis.css`) | **1.1.13** | Smooth Scrolling option. `lerp` from strength. Desktop, non-Safari only. Paused while fancyBox is open; destroyed while the Material off-canvas is open. |
| **anime.js** (`anime.min.js`) | **3.2.1** | Letter text effects, sticky-section timelines, column translate, counters… |
| **jQuery Transit** (`transit.min.js`) | **0.9.9** | `.transition()` column/image entrances with jQuery easing names |
| jQuery Easing (`jquery.easing.min.js`) | — | easing names |
| **Waypoints** (`waypoints.js`) | — | Scroll-trigger for all entrances |
| **Flickity** (`flickity.js` + `flickity-fade.js`) | — | Carousel, Simple Slider (fade), Gallery, Post Loop carousel, testimonials |
| **fancyBox** (`jquery.fancybox.js`) / **Magnific** (`magnific.js`) | **3.5.7** / — | Theme lightbox (default fancyBox3) |
| **Lottie** (`lottie-player.min.js` + `elements/nectar-lottie.js`) | lottie-web **5.13.0** | Lottie element |
| **Leaflet** (`leaflet.min.js`) | **1.9.4** | Interactive Map (Leaflet) |
| **Vivus** (`vivus.min.js`) | **0.4.2** | Linea icon line-drawing |
| **Parallax.js** (`parallax.js`, handle `nectar-parallax`) | — | Row *Mouse Based Parallax Scene* |
| twentytwenty (`jquery.twentytwenty.js`) | — | Image Comparison |
| fullPage (`jquery.fullPage.min.js`, bundles **iScroll 5.2.0**) | — | Page *Fullscreen Rows* |
| Isotope (`isotope.min.js`) | **2.2.2** | Portfolio / legacy masonry, filters |
| sticky-kit (`stickkit.js`) | — | *JavaScript Powered* sticky column |
| imagesLoaded, hoverIntent, Superfish, TouchSwipe, Modernizr, IntersectionObserver polyfill, jquery.mousewheel, select2, infinitescroll | — | Utilities (menus, touch, blog infinite scroll, select styling) |
| Legacy sliders: flexslider, caroufredsel, owl.carousel | — | Old gallery / carousel types |
| PIXI (`pixi`, + `elements/nectar-liquid.js`) | — | Legacy `displace-filter` BG animation (no longer offered in the dropdowns) |
| CountUp (inline in `init.js`) | — | Milestone *Count To Value* (2.2 s) |
| parallaxImg (inline in `init.js`) | — | Fancy Box *Parallax Hover Effect* tilt |
| Salient element scripts (`js/build/elements/`) | — | animated-gradient, blog, chat-thread, **color-change-bg**, **content-trail**, **fit-text**, full-page-rows, leaflet-map, liquid, lottie, **post-grid-stacked**, **sticky-media-sections**, testimonial-slider, **text-inline-images**, text-outline |

- **Not shipped:** GSAP / ScrollTrigger, Swiper, Barba / Swup, Locomotive.
- **No `prefers-reduced-motion` handling** anywhere in the theme CSS or JS.
- **Smooth scroll is Lenis.** It is not native CSS smooth scroll, and not a custom lerp.
- Page transitions (modern) use the native **View Transitions API**, with keyframes generated in `css/custom.php`.

---

## 6. What this means for the SGP demo (build rules)

1. **Every section maps to one Row (or Section) + Columns.** Hover cards = Column with *BG Hover Color + Hover Opacity + Shadow + Radius + Column Link*, or Fancy Box. Do not invent card behaviours Salient cannot reproduce.
2. **Only animate with the effects in §1 and the values in §3.** Tag them in the HTML (`data-salient="Inner Column | Mask Reveal | Bottom/Straight"`).
   - Entrances: 750 ms easeOutCubic (theme default). A demo-level 1300 ms is fine if Theme Options will be set to match.
   - Mask reveals: 1.3 s.
   - Animated Text: 1.2 s `(.25,1,.5,1)`.
3. **Hero:**
   - Row video/image BG + *Parallax Subtle (0.20)* or *BG Layer Zoom Out Slowly (8 s)*, + Color Overlay (simple or advanced gradient).
   - Headline: *Animated Text → Word Blur/Reveal + Stagger*.
   - CTA: *Button → Arrow Circle Animation* or *Text Reveal Wave*, Rounded / Pill.
4. **Header:** Transparent + *Permanent Transparent* (row Text Color drives light/dark) + *Hide Until Needed* + optional blur. Off-canvas *Fullscreen Cover Split* or *Slide Out From Side*.
5. **Services:** Post Loop Builder on a "Paslaugos" CPT (Vertical List with Featured Image Follow, or Grid with the View indicator), or *Sticky Content Sections* (Pinned, Blurred Scale + Stacked), or Horizontal List Items.
6. **Numbers:** Milestone *Count To Value*, with staggered delays.
7. **Coverage:** Interactive Map (Leaflet, greyscale, Nectar Animated markers). A dark map needs the Google type (API key).
8. **FAQ:** Toggle Panels *Animated Circle* or *Minimal Shadow*.
9. **Anything outside this list** (custom cursor, progress bar, magnetic buttons, GSAP scrubs, reduced-motion): keep it out of the demo, or flag it as "custom CSS/JS via Theme Options → Custom CSS/JS or Raw HTML".

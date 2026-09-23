# Salient elements and motion reference (for the SGP v2 demo)

This file describes what the Salient theme can build natively. The static HTML demo should use only these effects, so a WordPress developer can rebuild it 1:1 with Salient's page builder and theme options.

- **Version checked:** Salient **18.3.0** (released Sep 17, 2026). It bundles Salient WPBakery 8.7.3 and Salient Core 3.1.6.
- **Research date:** 2026-09-23.
- **Sources:**
  - themenectar.com/docs/salient/: every element, row, column and theme-option page, plus the changelogs for versions 10.0 to 18.3.
  - Live DOM of the demos Signal, Harbor, Tether, SaaS, Architect, Portfolio Layered, Portfolio Quantum, Resort, Nonprofit, Mag, Corporate 3, Business 3, Agency, Startup, Wellness, Photography and Freelance, and of the element showcase pages under `/salient/elements/*`.
  - The theme's own JS files: `init.js`, `nectar-smooth-scroll.js` and others.

**Legend:**
- No tag: confirmed in the current 18.x documentation.
- `[DOM]`: seen in a live demo's markup. Labels are inferred from the class or `data-*` values.
- `[CL x.y]`: confirmed only in the changelog for version x.y.
- `(unconfirmed)`: I could not verify it. Do not rely on it.

**Names changed in v18.** The WordPress developer will see these names in the builder:

| Old name (older tutorials) | Current name in the builder |
|---|---|
| Split Line Heading | **Animated Text** |
| Call to Action | **Button** |
| Button (old) | **Legacy Button** |
| Single Image / Image with Animation | **Image** |
| Sticky Media Sections | **Sticky Content Sections** |
| Text with Inline Images | **Text With Inline Media** |
| Post Grid | **Post Loop Builder** |
| Tabbed Section | **Tabs** (the Add Element window still says "Tabbed Section") |

**Grid facts:**
- Breakpoints: phone **≤690px**, tablet **691–999px**, desktop **≥1000px**.
- Container width: max **1425px** with Extended Responsive on (can be raised).
- Entrance animations are **off on phones** by default. Theme option: *Page Builder Element Animations On Mobile Devices*.
- Recent demos use **1300ms easeOutCubic** for column and image animations.

---

## 0. The 20 most useful elements for a premium logistics site

1. **Row video background + Parallax Background Media On Scroll (Subtle) + Advanced gradient Color Overlay.** Cinematic hero. Video backgrounds can use parallax since 17.0.
2. **Header Permanent Transparent, Hide Until Needed, background blur.** The header recolors itself from each row's Text Color (light/dark).
3. **Animated Text** (Word Reveal/Blur with stagger, Fit Text to Container) for the H1s.
4. **Animated Text → Scroll position: Opacity** for a long mission or USP sentence that lights up as you scroll.
5. **Text With Inline Media** for short looping clips (truck, warehouse, port) inside the headline. Use the *Circle Mask Reveal* animation.
6. **Milestone** set to *Count To Value* for fleet size, countries, km/year and on-time %. Stagger the delays.
7. **Sticky Content Sections → Sticky Scroll Pinned Sections** (Stacking effect or Blurred Scale) for service chapters: FTL/LTL, express, warehousing.
8. **Sticky Content Sections → Horizontal Scrolling** for the process or timeline, or a fleet gallery. Desktop only.
9. **Sticky Content Sections → Sticky Media, Scrolling Content** for "how a shipment moves". The media swaps as each text block arrives.
10. **Column animation Mask Reveal** (straight or circle shape, directional) and **Reveal From Left/Right/Bottom** for image cards.
11. **Column → Scroll Position Advanced** (e.g. Scale 0.85 → 1, Translate Y) for "scroll-scale" imagery.
12. **Row Background Layer Animation → Clip Path Inset** with the *Scroll Position* trigger, for a full-bleed image that opens up as you scroll.
13. **Fancy Box** (*Description on Hover* or *Parallax Hover Effect*, which is a 3D tilt) for service tiles.
14. **Post Loop Builder → Vertical List** with the hover effect *featured image follow*, or **Horizontal List Item** (color fill flips up on hover), for routes, destinations or services.
15. **Scrolling Text** marquee for routes (e.g. "Vilnius ✱ Berlin ✱ Paris"). Use Custom Symbol divider with *Spin on Scroll*, Move on Scroll, and alternate solid and outlined text.
16. **Carousel (Flickity) with Autorotate → Ticker + Mask Edges** for partner logos. The **Clients** element with *Greyscale to Color* is the simpler alternative.
17. **Testimonial Slider** in the *Multiple Visible* style, with a shadow on the active item.
18. **Interactive Map** (Leaflet, greyscale, *Nectar Animated* pulsing markers) or **Image With Hotspots** on a Europe map to show coverage.
19. **Color Change Section** on rows, so the page background shifts, for example dark → light → brand orange.
20. **Motion finishing:**
    - Button types *Arrow Circle Animation* and *Text Reveal Wave*.
    - Video Lightbox with *Play Button With Image – Mouse Follow*.
    - Toggle Panels in the *Animated Circle* style for the FAQ.
    - Off-canvas menu *Fullscreen Split*.
    - View Transitions *Vertical Reveal*.
    - Lenis smooth scroll.

**Not native** (needs custom CSS/JS): a global custom cursor, magnetic buttons and a scroll progress bar.

---

## 1. Page builder elements

### 1.1 Layout: Row, Inner Row, Section, Column

**Row** is the horizontal band. Most scroll and background effects live here.

| Option | What it gives you / values |
|---|---|
| Type | In Container · Full Width Background · Full Width Content |
| Full Height Row | Full height of the window. Content position: Middle / Top / Bottom / Full Height. Responsive Height and Min Height since 18.0 (svh/dvh supported). |
| Layout | Column Margin (none → 100px or custom), Equal Height Columns, Column Content Alignment, Column Direction per device (row-reverse / column-reverse) |
| Flexbox | Responsive flex controls for "Bento" layouts [CL 18.0] |
| Spacing / Transform | Padding and Margin per device; negative margin allowed, for overlaps. **Transform:** Translate X/Y and Scale per device (static). |
| Text Color | Light / Dark / Custom. **Drives the Permanent Transparent header color** as the header passes the row (`data-midnight` [DOM]). |
| Rounded Edges | Border radius, applied to the background, the inner content, or both |
| Background image | Preload option; CSS background or `<img>`; lazy load; hide on mobile; position and repeat |
| Video Background | YouTube, or MP4 + WebM (+OGV); preview image for mobile; lazy load |
| **Animated Gradient** | "Lava-lamp" blurred colour blobs; 2 colors, speed, color mix |
| **Mouse Based Parallax Scene** | Up to 5 image layers that move with the pointer, each with its own strength |
| Color Overlay | **Advanced:** multi-stop linear or radial gradient with its own opacities. **Simple:** 1–2 colors plus a strength value. |
| **Shape Divider** | 15 shapes: Curve, Curve Opacity, Curve Asym. (+Alt), Tilt (+Alt), Triangle, Fan, Mountains, Waves, Waves Opacity (+2), Clouds, Speech, Straight Section. Top, bottom or both; height per device; "Bring to front" |
| **Background Layer Animation** | Fade In · Zoom Out · Zoom Out Reveal · Slight Zoom Out Reveal · Zoom Out Slowly · **Clip Path Inset**. Clip Path Inset triggers *Triggered Once* or *Scroll Position* and applies to the background or the whole row. |
| **Parallax Background Media On Scroll** | Subtle / Regular / Medium / High / Fixed In Place. The demos mostly use Subtle. Works on video backgrounds too [CL 17.0]. The DOM also shows a `parallax_effect--parallax_fade` variant on the Harbor hero [DOM]; option label unconfirmed. |
| **Color Change Section** | The page background animates to this row's background color on scroll, and the text color follows [CL 18.0]. |
| **Sticky Row** | Top of Window / Bottom of Window / Top Below Nav Bar; can stay on mobile |
| Advanced | Row ID for anchors (animated anchor scroll is a theme option), z-index, overflow, device visibility, "Disable Ken Burns BG effect", disable row |

- **Inner Row:**
  - Relative or absolute positioning per device, with offsets.
  - Minimum Width, to break out of the column.
  - Max width.
  - Pointer events.
  - Backdrop filter [CL 18.0].
- **Section** [CL 18.0]: a container around several rows. It supports shape dividers and flexbox.
- **Page Full Screen Rows** (page metabox): fullPage.js-style section-by-section scrolling with dot navigation and row animations. It hijacks scrolling for the whole page, so avoid it for SGP.

**Column** carries most of the styling and entrance motion.

| Option | What it gives you / values |
|---|---|
| Padding / Margin / Transform | Per device. Negative margins allowed. Translate X/Y and Scale. |
| Element Direction and Spacing | Stacked or Inline Horizontal per device; element gap 5–50px; Centered Content |
| **Sticky Content** | CSS or JS powered. Top / Middle / Bottom. Optional on mobile. This is how you get a sticky caption beside a scrolling list. |
| Background | Color **+ Hover Color + Opacity / Hover Opacity** (the tint thins on hover). Image (stack order; can sit in front of the color), video background, **Backdrop Filter: Blur** (frosted glass), **Mask** (see below), Advanced gradient overlay |
| Shadow / Radius / Borders | Box shadow Small → Very Large, or custom. Border radius. **Column Borders:** Solid, Dashed, Double, Double Offset, plus **Animated Column Borders** that draw on entrance [DOM] |
| **Column Link** | The whole column becomes one link. Hover effects inside it stop firing, so put the hover on the column (bg hover). |
| **Column Animation Type** | **Triggered Once When Visible:**<br>• Fade In; Fade In From Left / Right / Bottom / Top ("From Top" [CL 18.3]); Slight Fade In From Bottom [DOM]<br>• Grow In; Zoom Out [CL 10.0]; Slight Twist [CL 10.5]; Flip In Horizontal / Vertical<br>• **Reveal From Left / Right / Top / Bottom** (clip) [DOM]<br>• **Mask Reveal** with shape Straight or Circle and a direction, e.g. left, left_bottom, right_bottom [DOM]<br>• Rotate Reveal [CL 12.0]<br>**Scroll Position Animation:** Move Y or Move X axis, Movement Intensity.<br>**Scroll Position Advanced:** start and end Translate X/Y and Scale, plus a Viewport Trigger Offset. |
| Background Layer Animation | Animates only the column background layer (e.g. Zoom Out Reveal) |
| Delay / Easing | Delay in ms (stagger 0/150/300). **Custom easing per column** overrides the global setting [CL 15.0] |
| Max width / z-index / position / overflow | Max width now has alignment [CL 18.3]. Overflow hidden is needed for mask and zoom effects. |

**Mask** is a tab on the Image and Column elements, not an element of its own.
- Shapes: Circle, **Bottom Blur Gradient**, Triangle, Parallelogram, Arch, Rhombus, Star, Heptagon, Ellipse, Lightning, 4 quarter-circles, Cross, or a Custom PNG.
- Size: Contain / Cover / Custom %.
- Alignment can be set per device.

**Positioning** is a tab on Image, Button, Badge, Icon, Lottie, Content Trail and Animated Shape.
- Position: Default, Relative or Absolute, per device.
- Offsets: top / right / bottom / left.
- Translate X/Y and z-index.

### 1.2 Typography and animated text

| Element | What it does | Motion options |
|---|---|---|
| **Animated Text** (ex Split Line Heading) | Heading split into lines, words or letters | **Text Effect:**<br>• Word: Reveal / Blur / Fade / Rotate / Twist<br>• Single letter from bottom: Reveal / Blur / Fade<br>• Single letter from top: Reveal / Blur / Fade<br>• **Scroll position: Opacity** (letters brighten with scroll)<br>• None<br>**Other controls:** Stagger, Animation Delay, Animation Offset, **Fit Text to Container**, Max Width, clamp sizing, Link plus a *Link Mouse Indicator* (custom cursor bubble over the text). DOM: `.nectar-split-heading[data-text-effect]` |
| Animated Title (legacy, no doc page) | Heading with a colored strip | Styles **Color Strip Reveal** and **Hinge Drop** [DOM] |
| **Highlighted Text** | Mark words in italics to highlight them | Styles:<br>• **Full Text BG Cover** (marker sweep)<br>• **Half Text BG Cover** [DOM]<br>• Fancy Underline<br>• Regular Underline (draws itself)<br>• Text Outline<br>• **Hand-Drawn Scribble** (circle, underline, strike…; 0.8–1.8s)<br>Gradient highlight color. Delay for staggering. |
| **Text With Inline Media** | Up to 4 images or **MP4 clips** inside a line of text | Animation: None / Scroll Reveal / **Circle Mask Reveal** / Circle Crop. Also stagger [DOM], roundness, inherit heading typography. |
| **Scrolling Text** | Marquee band | Direction Standard or Reverse. Speed Slowest → Fast, or Static. **Move on Scroll** (scroll-driven speed) [CL 16.0]. Custom Symbol divider with **Spin on Scroll**. Text Outline on all or alternating copies. Image-filled letters plus a background image animation (e.g. `ro-reveal-from-bottom` [DOM]). **Mask Edges** and custom spacing [CL 18.0]. |
| **Rotating Words** | Fixed text with a middle word that cycles (wipe) | Seconds between words; separate font family for the rotating word; entrance animation; mobile static option |
| Responsive Text | Fluid `clamp(min, vw, max)` text | Line height and text indent; `.nectar-link-underline-effect` [DOM] |
| Gradient Text | Heading filled with a theme gradient | Horizontal or diagonal |
| Morphing Outline | Outline around a word that morphs its shape on hover | Border thickness; start and hover color |
| Badge | Eyebrow pill or minimal line | **Backdrop blur** [DOM `backdrop_filter_blur_12`]; see-through style |
| Price Typography [CL 15.0] | Large price display | (unconfirmed options) |
| Fancy Unordered List / Icon List | Check or dot lists; icon or number lists | Staggered entrance animation; link hover style Animated Underline |
| Divider | Line or spacer | The line draws itself in (delay) |

### 1.3 Media

| Element | What it does | Motion / hover options |
|---|---|---|
| **Image** | Single image with extras | **Entrance:**<br>• Fade In; Fade In From Left / Right / Bottom / Top<br>• Grow In; Slide Up; Flip In Horizontal / Vertical<br>• Reveal Rotate From Top / Bottom / Left / Right<br>**Looped:** Rotate.<br>**Scroll movement:** Move Y or X, intensity −5…5.<br>**Hover:** Zoom In / **Zoom In Crop** / Color Overlay.<br>**Layout:** **Max Width 100–250%** (image hangs outside its column) or custom per device; Fit to Container plus object position; Mask tab; Positioning tab.<br>**Other:** lightbox (images and video); shadow presets or drop-shadow filter; *Image Loading* (lazy or skip). For a clip or mask reveal on an image, wrap it in an Inner Column with *Mask Reveal* or *Reveal From X*. |
| **Cascading Images** | Up to 4 stacked layers with offset, rotation (±20°) and scale | Per-layer entrance (Fade…, Grow In, **Grow In Reveal**, Flip In); **parallax scrolling** between layers [CL 11.0]; shadows |
| Image Gallery | 6 types: Basic Slider, Nectar Slider, **Flickity**, Flickity Static Height, **Image Grid** (masonry), **Parallax Image Grid** | Grid hovers: Meta on hover w/ zoom, Meta overlaid w/ zoom, Meta from bottom… Flickity extras: ticker, image parallax, stagger columns, scale when dragging, mask edges, free scroll |
| **Image With Hotspots** | Draggable markers on an image | Plus sign or numbered markers; tooltip on hover, click or always |
| **Image Comparison** | Before/after drag handle | twentytwenty library |
| **Video Lightbox** | YouTube or Vimeo in a lightbox | Link styles:<br>• Play Button<br>• Play Button With Text<br>• Play Button With Image<br>• **Play Button With Image – Mouse Follow**<br>• Nectar Button<br>Colored Button **Pulse**. Hover: Zoom BG Image or Zoom Button. **Parent Row BG Hover Relationship** zooms the hero background on hover. |
| **Self Hosted Video** (Player) | MP4/WebM player | Play button can **Follow Mouse**; lightbox trigger mode; lazy load; autoplay when scrolled into view [CL 15.0]; aspect ratio per device |
| **Lottie Animations** | JSON vector animation | Trigger: Autoplay / Play when visible / **Scroll Position Seek** / Hover (also when the parent column is hovered [CL 16.0]); start and end frames; speed |
| Circle Images | Overlapping **avatar stack** plus a "+12" counter circle (social proof) | Fade In entrance. Not a "circle image" element. |
| **Content Trail** [18.0] | Images or text strings spawn along the cursor path | In: Scale / Circle Mask. Out: Scale / Fade. Frequency, duration, lerp, random rotation. |
| Animated Shape [CL 15.0] | Decorative shape (e.g. half circle) | Scroll parallax movement [DOM saas] |
| Nectar Slider (plugin, legacy) | Old full-width slider | Ken Burns, parallax. For new builds use Carousel → Simple Slider. |

### 1.4 Interactive and hover

| Element | What it does | Motion / hover options |
|---|---|---|
| **Fancy Box** | Linked tile | Styles:<br>• **Bottom Color Bar Hover Effect** (default)<br>• **Color Box Hover Effect**<br>• Color Box Basic<br>• **Parallax Hover Effect** (layered 3D tilt that follows the mouse, `parallaxImg` library)<br>• **Description on Hover** (background Long or Short Zoom)<br>• **Image Above Text** (underline draws in)<br>Also overlay opacity and hover opacity, and a staggered entrance. "Movement" styles: (unconfirmed, not found). |
| **Flip Box** | Card that flips in 3D on hover (tap on touch) | Directions: Horizontal To Left / Right, Vertical To Bottom / Top; separate front and back backgrounds |
| **Horizontal List Item** | Table-like row with 1–4 columns, full-row link and optional CTA | Style *Bottom Border, Color Hover Effect*: an accent fill flips up on hover and the text turns white. Also Full Border, **Border Animation** (rule draws in). It does **not** reveal an image on hover; for that use the Post Loop Builder Vertical List. |
| **Button** (ex CTA) | Buttons and animated text links | Types:<br>• Basic<br>• See Through<br>• **Arrow Animation**<br>• **Arrow Circle Animation**<br>• Curved Arrow Animation<br>• **Underline**<br>• **Text Reveal Wave**<br>• Text Reveal<br>• Material Button<br>• **Next Section Button**<br>Hover colors for background, text and border. Roundness. **Backdrop blur** [DOM]. Presets for style, roundness and size [CL 18.2]. Stretch alignment. |
| Legacy Button | Old button | Regular / See Through / Gradient / Gradient Reverse / **See Through Solid On Hover** / See Through 3D [DOM]; sizes up to Extra Jumbo; optional WPBakery CSS Animation (Animate.css: bounce, swing…) [DOM]. "Regular W/ Tilt", "Regular w/ arrow" and a "Hover Effect: shadow/scale" option: (unconfirmed). |
| **Icon** | Single icon (Font Awesome, Iconsmind, Linea, Steadysets, Linecons, Brands, or an image) | Entrance animation (line icons draw via Vivus (unconfirmed which libraries)); **Pulsating Circle**; **Circle Pulse**; hover color |
| **Sticky Content Sections** | Scroll choreography with a parent and child sections | **Type:**<br>• **Sticky Media, Scrolling Content:** media swaps; media width 40–75% and height 50–100vh.<br>• **Sticky Scroll Pinned Sections:** effects None / **Overlapping** / **Scale** / **Blurred Scale** / **Fade Scale** / **Stacking**; Stacked Appearance; Section Navigation dots.<br>• **Horizontal Scrolling:** effect None or Stacking; section width 25–100vw; desktop >1000px only.<br>• **Layered Card Reveal:** stack of cards.<br>Effect on/off per device. Subtract Navigation Height. |
| Page Submenu | Page-level jump-link bar | **Sticky** once scrolled past |
| Interactive Map | Leaflet (no API key) or Google | **Nectar Animated** pulsing markers, greyscale, extra hue, Ultra Flat, dark scheme, custom marker image |
| Chat Thread [18.0] | Animated chat UI | Fade In or **Typing** (with loop); auto height |
| Team Member | Staff card | Meta Overlaid (wash clears on hover) · Meta Overlaid alt · Bio Modal styles (image parallax in the modal) |
| Clients | Logo row | **Greyscale to Color** or opacity on hover; fade in one by one; turns into a carousel |

### 1.5 Sliders and carousels

| Element | Styles and notable options |
|---|---|
| **Carousel** → **Simple Slider** (Flickity) | Slide or Fade transition; **Parallax Images**; aspect ratio or % of screen height; arrows inside or overlapping the slider; pagination; touch (drag) indicator; **Emit slide color to row background** |
| **Carousel** → **Flickity** | Styles **Default** and **Fixed Text Content Fullwidth** (fixed text block beside cells that run off the edge)<br>• Columns per breakpoint; shrink column width (peek); Adaptive Height; Center columns<br>• **Mask Edges**; **Subtle Item Scale When Dragging**; overflow visible<br>• Controls: Pagination / Arrows / Arrows Overlaid / **Touch & Total indicator**<br>• Autorotate → **Ticker** (continuous), with Ticker direction [CL 17.0]<br>Owl and carouFredSel are deprecated. |
| Testimonial Slider | **Basic** / **Minimal** (counter plus arrows) / **Multiple Visible** / **Multiple Visible Minimal**; shadow on the active item; star ratings; disable height animation |
| Post Loop Builder → Carousel | Posts or projects in a carousel with the same controls |
| Image Gallery → Flickity | See 1.3 |

### 1.6 Content and data

| Element | What it does / notable options |
|---|---|
| **Post Loop Builder** | Queries posts, portfolio projects or any CPT (a "Services" CPT works).<br>**Display type:** Grid (4 masonry variants, filters, Load More) · Carousel · **Stack** (Overlapping / Scale / **Blurred Scale** on scroll).<br>**Item styles:**<br>• Content Overlaid on Featured Image<br>• **Featured Image Mouse Follow on Hover** (titles only; the image follows the cursor)<br>• Content Under Featured Image (card with hover color)<br>• Content Next to Featured Image<br>• **Vertical List** (hover effects: reveal featured image, image follows cursor [DOM `vert_list_hover_effect_featured_image_follow`], recolor row, nudge)<br>**Hover effects:** BG Zoom / Slow BG Zoom / Animated Underline / Animated Underline Zoom.<br>**Other:** color overlay with hover opacity; **Mouse Indicator** ("View"/"Read" bubble in Default, See Through or Small Tooltip style, with blurred background); image parallax; entrance Fade in from bottom or right, or **Zoom out reveal**, with stagger and easing. |
| Portfolio (Salient Portfolio plugin) | Project styles:<br>• Meta below thumb w/ links on hover<br>• Meta on hover + entire thumb link<br>• Meta on hover w/ zoom<br>• Title overlaid w/ zoom (+alt)<br>• Meta from bottom on hover<br>• Meta Overlaid Bottom Left<br>• **Meta + 3D Parallax on hover**<br>Masonry and sortable filters. |
| **Tabs** ("Tabbed Section") | Styles: Default, Material, Minimal, Minimal Alt, Minimal Flexible Width, **Toggle Button** (2 tabs), Vertical, Vertical Material, **Vertical Sticky Scrolling**. Settings for tab change animation, content animation and link hover animation. Per-tab CTA. Deep-linkable. |
| **Toggle Panels** | Default, **Animated Circle**, Minimal, **Minimal Shadow**, Inline Small; accordion mode; deep linking with auto scroll [CL 18.1] |
| **Milestone** | Animation Effect: **Count To Value** / **Motion Blur Slide In** / None; single decimal; symbol before or after (can be superscript); delay |
| Progress Bar | Fills to its % on scroll; gradient colors allowed |
| Pricing Table | Legacy. Build pricing from rows and columns instead. |
| Star Rating | 1–5 stars in half steps, with a text label |
| Food Menu Item | Not relevant for SGP |
| Shape Divider | A Row or Section setting, see 1.1 |

### 1.7 Forms, global and miscellaneous

- **Forms:** Salient styles the output of **Fluent Forms** (full compatibility [CL 18.0]; Signal uses it), WPForms and Contact Form 7. Theme Options → Form Styling covers fancy checkboxes and the submit button style. There is a `nectar-inline-subscribe-form` class for one-line forms.
- **Global Sections:** reusable page-builder blocks. Locations include:
  - "In Navigation Top (Before Scrolling)" [CL 18.0]
  - mega menu panels
  - off-canvas content
  - footer
  - before footer
  - blog archive loop

  They carry display conditions. The **Global Section element** drops one into any page.
- **Mega Menu:** built from a Global Section attached in Appearance → Menus, or from nested menu items. Menu items can have a video background and a CTA [CL 16.0].
- **Raw HTML / Raw JS** elements, plus **Custom CSS Code / Custom JS Code** in Theme Options → General Settings, plus an *Extra Class Name* on every element. This is how the "not native" effects get added.
- **Salient Studio:** a library of prebuilt section templates (inserted as normal rows).
- **Page Header metabox** (legacy hero):
  - Image, video or HTML5 Canvas (particles).
  - Scroll effects **Parallax** and **Box Roll**.
  - Fullscreen with an animated mouse-scroll arrow.
  - Text effect.

---

## 2. Global theme options that affect motion

| Area | Options (values) | Tell-tale in the DOM |
|---|---|---|
| **Smooth scroll** | *Smooth Scrolling* powered by **Lenis** [CL 17.0], plus *Smooth Scrolling strength* [CL 17.0.2] | `nectarOptions.smooth_scroll="true"`, `smooth_scroll_strength:"60"` (Signal) |
| **Animation easing and timing** | *Column/Image Animation Easing*: jQuery easing names, e.g. linear, easeOutCubic, easeOutQuart, easeOutExpo, easeInOutCubic. *Column/Image Animation Timing* in ms (default 750). | `body[data-cae]`, `body[data-cad]`. Demos use 1300/easeOutCubic (Signal, Harbor, Tether), 1500/easeOutQuart (Architect), 1350/easeOutExpo (Corporate 3). |
| Mobile animations | *Page Builder Element Animations On Mobile Devices* (off by default); each element can disable its own animation on mobile | `data-m-animate` |
| **Page transitions** | *Transition Method*:<br>• **View Transitions API** (modern), effects **Fade**, **Horizontal Gradient Wipe**, **Vertical Reveal**, **Vertical Reveal Scale**<br>• **Simulated with JS** (legacy), effects *Fade with loading icon*, *Center mask reveal* and *Horizontal Swipe* (`data-apte=horizontal_swipe` on Startup [DOM]); loading icon Default or Material, or a custom image<br>Also: disable on mobile. | `nectarOptions.view_transitions_effect="vertical-reveal"` (Signal), `data-ajax-transitions`, `data-apte` |
| **Custom cursor** | **No site-wide custom cursor option.** Only element-level *Mouse Indicators*:<br>• Post Loop Builder "View" bubble<br>• Carousel/Gallery drag indicator<br>• Video Lightbox/Player follow-mouse play button<br>• Animated Text link indicator<br>• Content Trail<br>`init.js` and the CSS contain only `.nectar-view-indicator`, `.nectar-drag-indicator` and `.nectar-close-indicator`. | none on `body` |
| **Buttons** | *Button Styling*: Default / Slightly Rounded / Slightly Rounded W/ Shadow / Rounded / Rounded W/ Shadow. Button element presets [CL 18.2]. | `data-button-style` = `rounded`, `rounded_shadow`, `slightly_rounded_shadow` |
| Theme skin | Material / Ascend / Original. All new demos use Material. | `body.material` |
| **Header effects** | **Transparent Header** (starting and dark logos); **Header Permanent Transparent** (recolors per row); Header Inherit Row Color; **Hide Until Needed** (hides on scroll down, shows on scroll up); **Resize On Scroll** (shrink); **background blur (frosted)** [CL 15.0]; **gradient background blur** on the transparent header [CL 18.0]; BG opacity; **Header Navigation Entrance Animation** (Fade In / Zoom Out, with delay and easing); **Header Link Hover/Active Effect**: Animated Underline / Color Change / **Text Reveal** [CL 17.0]; general link styling (animated underline) | `data-permanent-transparent`, `data-hhun`, `data-header-resize`, `data-aie`, `.nectar-link-underline-effect` |
| Header layouts | Default · Centered Menu · Menu Left Aligned · Centered Logo Between Menu (+Alt) · Centered Menu Under Logo · Centered Menu Bottom Bar · Left Header · **Contained** (+auto width [CL 18.0]); Secondary Header Bar; mega menu full or contained width | `data-header-format` = default, centered-menu, menu-left-aligned, centered-logo-between-menu-alt |
| **Off-canvas menu** | **Slide Out From Side** (`slide-out-from-right`)<br>**Slide Out From Side Hover Triggered** (`slide-out-from-right-hover`)<br>**Fullscreen Cover Slide + Blur BG** (`fullscreen`)<br>**Fullscreen Cover Fade** (`fullscreen-alt`)<br>**Fullscreen Split** (`fullscreen-split`)<br>**Fullscreen Inline with Dynamic BG** (`fullscreen-inline-images`)<br>**Simple Dropdown**<br>Also: overlay strength, icon style and line width, social icons, bottom text, Global Section content. | `data-slide-out-widget-area-style` |
| Back to top | Back To Top Button, with an option to keep it on mobile | — |
| Anchor scroll | *One Page Scroll Support (animated Anchor Links)* | `data-animated-anchors` |
| **Lightbox** | *Theme Lightbox*: **fancyBox3** (recommended) or **Magnific**; Auto Lightbox Image Links | `data-ls="fancybox"` |
| Footer | **Footer Reveal Effect** (+shadow); a Global Section footer is recommended | `data-footer-reveal` |
| Body Border | Passepartout frame around the viewport, fixed or scrolling vignette [CL 17.0] | `data-body-border` |
| Parallax / video on mobile | Disable Parallax Backgrounds On Mobile; Disable Video Backgrounds On Mobile (uses the preview image) | `data-remove-m-parallax`, `data-remove-m-video-bgs` |
| Typography | **Fluid Typography** (root clamp) [CL 18.0]; local Google Fonts; units rem/em/px | — |
| Performance | Delay JavaScript Execution, lazy loading, Local Google Fonts, image preloading | `nectar-delay-javascript.js` |

---

## 3. JS libraries Salient ships

All confirmed by the `<script src>` list on the live demos and by strings in `init.js`, unless noted.

| Library | Used for |
|---|---|
| jQuery + jQuery Easing | Everything; easing names come from here |
| **anime.js** | Core animations such as text effects and counters (loaded on every demo) |
| **Lenis** (`nectar-smooth-scroll.js`, v1.1.13) | Smooth scrolling theme option |
| **Flickity** (2.3.x [CL]) | Carousel, Simple Slider, Flickity galleries, Post Loop Builder carousel, testimonials |
| **fancyBox 3** / **Magnific Popup** | Theme lightbox (one or the other) |
| Waypoints | Scroll-triggered entrance animations |
| Transit | CSS3 transitions via jQuery |
| imagesLoaded | Layout after images load |
| hoverIntent + Superfish | Dropdown menus |
| TouchSwipe | Touch gestures on sliders |
| sticky-kit (`stickkit.js`) | JS-powered sticky columns |
| Isotope | Portfolio / legacy masonry and filtering (not loaded on normal pages) |
| **Lottie** (`lottie-player.min.js` + `nectar-lottie.js`) | Lottie element |
| Vivus | SVG line-drawing (icons) |
| twentytwenty | Image Comparison |
| parallaxImg | Fancy Box "Parallax Hover" 3D tilt |
| fullPage.js (API calls in `init.js`) | Page Full Screen Rows |
| Swiper (strings in `init.js`) | Nectar Slider (unconfirmed which slider) |
| jquery.mousewheel, select2 | Mousewheel loads with the Box Roll page header on Agency (exact use unconfirmed); select2 styles select fields |
| Element scripts | `nectar-text-inline-images`, `nectar-content-trail`, `nectar-sticky-media-sections`, `nectar-color-change-bg`, `nectar-animated-gradient`, `nectar-fit-text`, `nectar-chat-thread`, `nectar-post-grid-stacked`, `nectar-text-outline`, `nectar-testimonial-slider`, `nectar-box-roll` |
| Not shipped | **GSAP / ScrollTrigger: no.** Swup/Barba: no. Page transitions use the native View Transitions API. Some text effects use CSS scroll-driven timelines (`.scroll-timeline` [DOM]). |

---

## 4. Design-to-Salient cheat sheet

| # | Modern effect in the demo | Salient element + option that reproduces it |
|---|---|---|
| 1 | Full-screen video hero with parallax | Row: Full Height Row + Video Background (MP4/WebM) + **Parallax Background Media On Scroll → Subtle** + Color Overlay → Advanced gradient |
| 2 | Hero image slowly zooming out on load | Row → Background Layer Animation → **Zoom Out Slowly / Slight Zoom Out Reveal** |
| 3 | Image that "opens up" or scales while scrolling | Row → Background Layer Animation → **Clip Path Inset + Scroll Position**; or Column → **Scroll Position Advanced** (Scale start 0.85 → end 1) |
| 4 | Headline revealing line by line or word by word | **Animated Text** → Word Reveal / Blur / Fade + Stagger |
| 5 | Letter-by-letter blur-in heading | **Animated Text** → Single letter from bottom → Blur |
| 6 | Paragraph that lights up as you scroll | **Animated Text** → Scroll position → **Opacity** |
| 7 | Marker highlight or hand-drawn circle on a keyword | **Highlighted Text** → Full Text BG Cover / Hand-Drawn Scribble |
| 8 | Video or photo pills inside a headline | **Text With Inline Media** → Videos + *Circle Mask Reveal* |
| 9 | Infinite marquee band (routes, services) | **Scrolling Text** (+ Move on Scroll, divider Spin on Scroll, outline on alternating copies, Mask Edges) |
| 10 | Logo ticker | **Carousel → Flickity → Autorotate: Ticker** + Mask Edges, or **Clients** (Greyscale to Color) |
| 11 | Animated counters | **Milestone** → Count To Value (stagger the delays) |
| 12 | Sticky stacking cards | **Sticky Content Sections** → Sticky Scroll Pinned Sections → *Stacking / Overlapping / Blurred Scale*; or **Post Loop Builder → Stack** for posts or CPT items |
| 13 | Horizontal scroll gallery or timeline | **Sticky Content Sections → Horizontal Scrolling** (desktop only; stacks on mobile) |
| 14 | Sticky image that swaps while the text scrolls | **Sticky Content Sections → Sticky Media, Scrolling Content** |
| 15 | Sticky left caption with a scrolling right column | Column → **Sticky Content** (CSS, Top) |
| 16 | Image mask or clip reveal on entrance | Inner Column → Animation **Mask Reveal** (Straight/Circle + direction) or **Reveal From Left/Right/Bottom**, with overflow hidden |
| 17 | Staggered fade-up cards | Column → Fade In From Bottom / *Slight Fade In From Bottom*, delays 0/150/300 |
| 18 | Elements drifting at different speeds (depth) | Image or Column → **Scroll Position Animation** (Move Y, intensity ±); Cascading Images parallax |
| 19 | Mouse-move parallax layers | Row → **Mouse Based Parallax Scene** (≤5 layers) |
| 20 | 3D tilt card on hover | **Fancy Box → Parallax Hover Effect**; or **Flip Box** for a two-sided card |
| 21 | Service tile with reveal-on-hover text | **Fancy Box → Description on Hover** (Long Zoom) or **Bottom Color Bar**; Column bg hover color + Column Link for custom cards |
| 22 | Horizontal hover list with image reveal | **Post Loop Builder → Vertical List** with the featured image reveal or follow hover effect (needs a CPT). For a static list without images use **Horizontal List Item** (color fill flips up). |
| 23 | Project grid with a "View" cursor bubble | **Post Loop Builder** → Add Mouse Indicator (Small Tooltip, blurred background) |
| 24 | Image trail following the cursor | **Content Trail** |
| 25 | Page background colour changing between sections | Row → **Color Change Section** |
| 26 | Animated gradient or "aurora" background | Row → **Animated Gradient** |
| 27 | Curved or angled section edges | Row → **Shape Divider** |
| 28 | Glassmorphism panels, pill buttons and header | Column → **Backdrop Filter Blur**; Button/Badge backdrop blur; header background blur |
| 29 | Before/after slider | **Image Comparison** |
| 30 | Hotspot or coverage map | **Image With Hotspots** (numbered, show on hover) or **Interactive Map** (Leaflet, greyscale, animated markers) |
| 31 | Tabs / accordion | **Tabs** (Minimal, Vertical Sticky Scrolling, Toggle Button) / **Toggle Panels** (Animated Circle, Minimal Shadow) |
| 32 | Testimonial slider | **Testimonial Slider** → Multiple Visible (+ active shadow) |
| 33 | Play-button video modal | **Video Lightbox** → Play Button With Image – Mouse Follow (+ Parent Row BG Hover Relationship) |
| 34 | Smooth scroll, page transitions, fullscreen menu | Theme Options: Smooth Scrolling (Lenis) · View Transitions *Vertical Reveal* · Off Canvas *Fullscreen Split* |
| 35 | **Custom cursor, magnetic buttons, scroll progress bar, text scramble or typewriter, cursor-reactive WebGL, SVG route-drawing on scroll** | **Needs custom CSS/JS.** Add them via Theme Options → Custom JS/CSS or a Raw JS element, attached to Extra Class Names. Lottie *Scroll Position Seek* can stand in for SVG route drawing. |

---

## 5. Handoff conventions for the static demo

- **Build from the parts in sections 1–4 only.** Tag each section and effect in the HTML so the developer can map it, for example `data-salient="Row | Parallax BG: Subtle | Color Change: #0E1116"` and `data-salient="Animated Text | Word Blur | stagger"`.
- **Recreate the motion with the same engines Salient uses**, so the feel matches after the rebuild: Lenis 1.1.x smooth scroll, Flickity 2.3 carousels, anime.js or CSS for entrances, fancyBox-style lightbox, CSS `clip-path` for Reveal/Mask. Avoid GSAP-only tricks such as pinned scrub timelines that go beyond Sticky Content Sections.
- **Timing defaults:**
  - Entrances: ~1300ms `cubic-bezier(0.215,0.61,0.355,1)` (easeOutCubic).
  - Staggers: 90–150ms.
  - Entrance starts when the element's top reaches 88% of the viewport height.
- **Mobile:**
  - Entrance animations are off by default.
  - Horizontal Scrolling stacks below 1000px.
  - Pinned sections can be turned off per device.
  - YouTube backgrounds do not play on mobile.
  - Always provide a poster image.
- **Respect `prefers-reduced-motion`** in the demo. Salient itself only exposes per-device switches.

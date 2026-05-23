# Brio — Platform Mapping

## 1. HTML / CSS / WEB

### Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

### CSS Custom Properties — Primary Mode

```css
:root {
  /* Colors */
  --background: #F5F6F6;
  --bg: var(--background);
  --surface1: #FFFFFF;
  --surface2: #EBECEC;
  --surface3: #D5D8DA;
  --border: #D5D8DA;
  --border-visible: #C5C8D1;
  --text1: #202223;
  --text2: #6D7175;
  --text3: #9EA3AA;
  --text4: #C5C8D1;
  --accent: #3C69B1;
  --accent-subtle: #EBF2FA;
  --success: #1B9500;
  --success-bg: #E8F8E8;
  --warning: #C48A00;
  --warning-bg: #FFF8E8;
  --error: #D3002F;
  --error-bg: #FDE8E8;

  /* Fonts */
  --font-display: "Inter", Helvetica, Arial, sans-serif;
  --font-body: "Inter", Helvetica, Arial, sans-serif;
  --font-mono: "JetBrains Mono", Menlo, Monaco, monospace;

  /* Type Scale */
  --text-display: 48px;
  --text-heading: 32px;
  --text-subheading: 22px;
  --text-body: 15px;
  --text-body-sm: 13px;
  --text-caption: 12px;
  --text-label: 11px;

  /* Spacing */
  --space-2xs: 2px;
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
  --space-4xl: 96px;

  /* Radii */
  --radius-cards: 16px;
  --radius-buttons: 4px;
  --radius-buttons-sm: 2px;
  --radius-inputs: 4px;
  --radius-tags: 999px;
  --radius-modals: 20px;

  /* Motion */
  --ease-fast: ease-in-out;
  --ease-medium: ease-in-out;
  --ease-slow: ease-in-out;
  --duration-fast: 150ms;
  --duration-medium: 300ms;
  --duration-slow: 500ms;

  /* Shadows — flat elevation strategy, no shadows */
  --shadow-1: none;
  --shadow-2: none;
  --shadow-3: none;
}
```

### Secondary Mode

```css
@media (prefers-color-scheme: dark) {
  :root {
    --background: #0E2130;
    --bg: var(--background);
    --surface1: #0B1A26;
    --surface2: #08131C;
    --surface3: #060D14;
    --border: #08131C;
    --border-visible: #0B1A26;
    --text1: #F5F6F6;
    --text2: #9EA3AA;
    --text3: #6D7175;
    --text4: #C5C8D1;
    --accent: #6FCFEB;
    --accent-subtle: #08131C;
    --success: #1B9500;
    --success-bg: #0B1A26;
    --warning: #C48A00;
    --warning-bg: #0B1A26;
    --error: #D3002F;
    --error-bg: #0B1A26;
    --shadow-1: none;
    --shadow-2: none;
    --shadow-3: none;
  }
}

/* Class-based toggle alternative */
.dark {
  --background: #0E2130;
  --bg: var(--background);
  --surface1: #0B1A26;
  --surface2: #08131C;
  --surface3: #060D14;
  --border: #08131C;
  --border-visible: #0B1A26;
  --text1: #F5F6F6;
  --text2: #9EA3AA;
  --text3: #6D7175;
  --text4: #C5C8D1;
  --accent: #6FCFEB;
  --accent-subtle: #08131C;
  --success: #1B9500;
  --success-bg: #0B1A26;
  --warning: #C48A00;
  --warning-bg: #0B1A26;
  --error: #D3002F;
  --error-bg: #0B1A26;
  --shadow-1: none;
  --shadow-2: none;
  --shadow-3: none;
}
```

---

## 2. SWIFTUI / iOS

### Font Registration

Brio uses system fonts on Apple platforms — no custom font registration required. Inter and JetBrains Mono are referenced by name for web only.

### Color Extension

```swift
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 6: (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default: (a, r, g, b) = (255, 0, 0, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue: Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}

extension Color {
    // Primary mode
    static let brioBackground = Color(hex: "F5F6F6")
    static let brioSurface1 = Color(hex: "FFFFFF")
    static let brioSurface2 = Color(hex: "EBECEC")
    static let brioSurface3 = Color(hex: "D5D8DA")
    static let brioBorder = Color(hex: "D5D8DA")
    static let brioBorderVisible = Color(hex: "C5C8D1")
    static let brioText1 = Color(hex: "202223")
    static let brioText2 = Color(hex: "6D7175")
    static let brioText3 = Color(hex: "9EA3AA")
    static let brioText4 = Color(hex: "C5C8D1")
    static let brioAccent = Color(hex: "3C69B1")
    static let brioAccentSubtle = Color(hex: "EBF2FA")
    static let brioSuccess = Color(hex: "1B9500")
    static let brioWarning = Color(hex: "C48A00")
    static let brioError = Color(hex: "D3002F")
}
```

For automatic dark/light switching, use Asset Catalog (`Colors.xcassets`) with "Any, Dark" appearances instead of hardcoded hex values. The hex extension above is for prototyping or single-mode use.

### Font Extension

```swift
extension Font {
    static func brioDisplay(_ size: CGFloat, weight: Font.Weight = .bold) -> Font {
        .system(size: size, weight: weight, design: .default)
    }
    static func brioBody(_ size: CGFloat, weight: Font.Weight = .regular) -> Font {
        .system(size: size, weight: weight, design: .default)
    }
    static func brioMono(_ size: CGFloat, weight: Font.Weight = .regular) -> Font {
        .system(size: size, weight: weight, design: .monospaced)
    }

    static let brioDisplayLarge = brioDisplay(48, weight: .bold)
    static let brioHeading = brioDisplay(32, weight: .bold)
    static let brioSubheading = brioBody(22, weight: .medium)
    static let brioBodyText = brioBody(15)
    static let brioBodySmall = brioBody(13)
    static let brioCaption = brioBody(12)
    static let brioLabel = brioBody(11, weight: .medium)
    static let brioDataBody = brioMono(13)
}
```

### Spacing & Radius Constants

```swift
enum BRIOSpacing {
    static let xxs: CGFloat = 2
    static let xs: CGFloat = 4
    static let sm: CGFloat = 8
    static let md: CGFloat = 16
    static let lg: CGFloat = 24
    static let xl: CGFloat = 32
    static let xxl: CGFloat = 48
    static let xxxl: CGFloat = 64
    static let xxxxl: CGFloat = 96
}

enum BRIORadius {
    static let cards: CGFloat = 16
    static let cardsFeatured: CGFloat = 16
    static let buttons: CGFloat = 4
    static let buttonsSmall: CGFloat = 2
    static let inputs: CGFloat = 4
    static let tags: CGFloat = 999
    static let modals: CGFloat = 20
}
```

### Dark/Light Mode

Use `@Environment(\.colorScheme)` for mode detection. For production apps, define all colors in an Asset Catalog with "Any, Dark" appearances for automatic switching. The Color extension above provides single-mode hex values; swap them for Asset Catalog references in production.

---

## 3. REACT / TAILWIND

### tailwind.config.js

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        surface: {
          1: "var(--surface1)",
          2: "var(--surface2)",
          3: "var(--surface3)",
        },
        border: {
          DEFAULT: "var(--border)",
          visible: "var(--border-visible)",
        },
        text: {
          1: "var(--text1)",
          2: "var(--text2)",
          3: "var(--text3)",
          4: "var(--text4)",
        },
        accent: {
          DEFAULT: "var(--accent)",
          subtle: "var(--accent-subtle)",
        },
        success: {
          DEFAULT: "var(--success)",
          bg: "var(--success-bg)",
        },
        warning: {
          DEFAULT: "var(--warning)",
          bg: "var(--warning-bg)",
        },
        error: {
          DEFAULT: "var(--error)",
          bg: "var(--error-bg)",
        },
      },
      fontFamily: {
        display: ["Inter", "Helvetica", "Arial", "sans-serif"],
        body: ["Inter", "Helvetica", "Arial", "sans-serif"],
        mono: ["JetBrains Mono", "Menlo", "Monaco", "monospace"],
      },
      fontSize: {
        display: ["48px", { lineHeight: "1.1", letterSpacing: "-0.02em" }],
        heading: ["32px", { lineHeight: "1.2", letterSpacing: "-0.01em" }],
        subheading: ["22px", { lineHeight: "1.3", letterSpacing: "0" }],
        body: ["15px", { lineHeight: "1.6", letterSpacing: "0" }],
        "body-sm": ["13px", { lineHeight: "1.5", letterSpacing: "0" }],
        caption: ["12px", { lineHeight: "1.4", letterSpacing: "0.02em" }],
        label: ["11px", { lineHeight: "1.3", letterSpacing: "0.04em" }],
      },
      spacing: {
        "2xs": "2px",
        xs: "4px",
        sm: "8px",
        md: "16px",
        lg: "24px",
        xl: "32px",
        "2xl": "48px",
        "3xl": "64px",
        "4xl": "96px",
      },
      borderRadius: {
        cards: "16px",
        buttons: "4px",
        "buttons-sm": "2px",
        inputs: "4px",
        tags: "999px",
        modals: "20px",
      },
      transitionTimingFunction: {
        fast: "ease-in-out",
        medium: "ease-in-out",
        slow: "ease-in-out",
      },
      transitionDuration: {
        fast: "150ms",
        medium: "300ms",
        slow: "500ms",
      },
      boxShadow: {
        1: "none",
        2: "none",
        3: "none",
      },
    },
  },
  plugins: [],
};
```

### Font Loading

Load fonts via Google Fonts `<link>` tag in the HTML `<head>` (see Section 1 above) or via `@fontsource` packages:

```bash
npm install @fontsource/inter @fontsource/jetbrains-mono
```

```js
import "@fontsource/inter";
import "@fontsource/jetbrains-mono";
```

### CSS Variables

Include the `:root` CSS custom properties from Section 1 in your global stylesheet (`globals.css` or `index.css`). The Tailwind config references these via `var(--token-name)` for automatic dark mode support.

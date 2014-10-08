// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "athena/util/fill_layout_manager.h"

#include "testing/gtest/include/gtest/gtest.h"
#include "ui/aura/window.h"
#include "ui/wm/public/window_types.h"

namespace athena {

TEST(FillLayoutManagerTest, ChildWindowSizedCorrectly) {
  scoped_ptr<aura::Window> parent(new aura::Window(NULL));
  parent->SetBounds(gfx::Rect(10, 20, 30, 40));
  parent->SetLayoutManager(new FillLayoutManager(parent.get()));

  scoped_ptr<aura::Window> child(new aura::Window(NULL));
  child->SetBounds(gfx::Rect(0, 0, 5, 10));

  EXPECT_NE(child->bounds().size().ToString(),
            parent->bounds().size().ToString());

  parent->AddChild(child.get());
  EXPECT_EQ(child->bounds().size().ToString(),
            parent->bounds().size().ToString());

  parent->SetBounds(gfx::Rect(0, 0, 100, 200));
  EXPECT_EQ(child->bounds().size().ToString(),
            parent->bounds().size().ToString());

  // Menu and tooltip should not be filled.
  scoped_ptr<aura::Window> menu(new aura::Window(NULL));
  menu->SetType(ui::wm::WINDOW_TYPE_MENU);
  menu->SetBounds(gfx::Rect(0, 0, 5, 10));

  EXPECT_EQ(menu->bounds().ToString(), "0,0 5x10");
  parent->AddChild(menu.get());
  EXPECT_EQ(menu->bounds().ToString(), "0,0 5x10");
  menu->SetBounds(gfx::Rect(0, 0, 100, 200));
  EXPECT_EQ(menu->bounds().ToString(), "0,0 100x200");

  scoped_ptr<aura::Window> tooltip(new aura::Window(NULL));
  tooltip->SetType(ui::wm::WINDOW_TYPE_TOOLTIP);
  tooltip->SetBounds(gfx::Rect(0, 0, 5, 10));

  EXPECT_EQ(tooltip->bounds().ToString(), "0,0 5x10");
  parent->AddChild(tooltip.get());
  EXPECT_EQ(tooltip->bounds().ToString(), "0,0 5x10");
  tooltip->SetBounds(gfx::Rect(0, 0, 100, 200));
  EXPECT_EQ(tooltip->bounds().ToString(), "0,0 100x200");
}

}  // namespace athena

// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/utf_string_conversions.h"
#include "ui/gfx/point.h"
#include "ui/gfx/rect.h"
#include "ui/gfx/render_text.h"
#include "views/controls/textfield/native_textfield_views.h"
#include "views/controls/textfield/textfield.h"
#include "views/test/views_test_base.h"
#include "views/touchui/touch_selection_controller.h"
#include "views/touchui/touch_selection_controller_impl.h"
#include "views/widget/widget.h"

namespace views {

class TouchSelectionControllerImplTest : public ViewsTestBase {
 public:
  TouchSelectionControllerImplTest()
      : widget_(NULL),
        textfield_(NULL),
        textfield_view_(NULL) {
  }

  virtual void SetUp() {
    Widget::SetPureViews(true);
  }

  virtual void TearDown() {
    Widget::SetPureViews(false);
    if (widget_)
      widget_->Close();
    ViewsTestBase::TearDown();
  }

  void CreateTextfield() {
    textfield_ = new Textfield();
    widget_ = new Widget;
    Widget::InitParams params(Widget::InitParams::TYPE_POPUP);
    params.bounds = gfx::Rect(0, 0, 200, 200);
    widget_->Init(params);
    View* container = new View();
    widget_->SetContentsView(container);
    container->AddChildView(textfield_);

    textfield_view_ = static_cast<NativeTextfieldViews*>(
        textfield_->GetNativeWrapperForTesting());
    textfield_view_->SetBoundsRect(params.bounds);
    textfield_->set_id(1);

    DCHECK(textfield_view_);
    textfield_->RequestFocus();
  }

 protected:
  gfx::Point GetCursorPosition(int cursor_pos) {
    gfx::RenderText* render_text = textfield_view_->GetRenderText();
    gfx::Rect cursor_bounds = render_text->GetCursorBounds(
        gfx::SelectionModel(cursor_pos), false);
    return gfx::Point(cursor_bounds.x(), cursor_bounds.bottom());
  }

  TouchSelectionControllerImpl* GetSelectionController() {
    return static_cast<TouchSelectionControllerImpl*>(
        textfield_view_->touch_selection_controller_.get());
  }

  void SimulateSelectionHandleDrag(gfx::Point p, int selection_handle) {
    TouchSelectionControllerImpl* controller = GetSelectionController();
    // Do the work of OnMousePressed().
    if (selection_handle == 1)
      controller->dragging_handle_ = controller->selection_handle_1_.get();
    else
      controller->dragging_handle_ = controller->selection_handle_2_.get();

    controller->SelectionHandleDragged(p);

    // Do the work of OnMouseReleased().
    controller->dragging_handle_ = NULL;
  }

  // If textfield has selection, this method verifies that the selection handles
  // are visible and at the correct positions (at the end points of selection).
  // |cursor_at_selection_handle_1| is used to decide whether selection
  // handle 1's position is matched against the start of selection or the end.
  void VerifySelectionHandlePositions(bool cursor_at_selection_handle_1) {
    if (textfield_->HasSelection()) {
      EXPECT_TRUE(GetSelectionController()->IsSelectionHandle1Visible());
      EXPECT_TRUE(GetSelectionController()->IsSelectionHandle2Visible());
      ui::Range selected_range;
      textfield_view_->GetSelectedRange(&selected_range);
      gfx::Point selection_start = GetCursorPosition(selected_range.start());
      gfx::Point selection_end = GetCursorPosition(selected_range.end());
      gfx::Point sh1 = GetSelectionController()->GetSelectionHandle1Position();
      gfx::Point sh2 = GetSelectionController()->GetSelectionHandle2Position();
      sh1.Offset(10, 0); // offset by kSelectionHandleRadius.
      sh2.Offset(10, 0);

      if (cursor_at_selection_handle_1) {
        EXPECT_EQ(sh1, selection_end);
        EXPECT_EQ(sh2, selection_start);
      } else {
        EXPECT_EQ(sh1, selection_start);
        EXPECT_EQ(sh2, selection_end);
      }
    } else {
      EXPECT_FALSE(GetSelectionController()->IsSelectionHandle1Visible());
      EXPECT_FALSE(GetSelectionController()->IsSelectionHandle2Visible());
    }
  }

  Widget* widget_;

  Textfield* textfield_;
  NativeTextfieldViews* textfield_view_;

 private:
  DISALLOW_COPY_AND_ASSIGN(TouchSelectionControllerImplTest);
};

// Tests that the selection handles are placed appropriately when selection in
// a Textfield changes.
TEST_F(TouchSelectionControllerImplTest, SelectionInTextfieldTest) {
  CreateTextfield();
  textfield_->SetText(ASCIIToUTF16("some text"));

  // Test selecting a range.
  textfield_->SelectRange(ui::Range(3, 7));
  VerifySelectionHandlePositions(false);

  // Test selecting everything.
  textfield_->SelectAll();
  VerifySelectionHandlePositions(false);

  // Test with no selection.
  textfield_->ClearSelection();
  VerifySelectionHandlePositions(false);

  // Test with lost focus.
  widget_->GetFocusManager()->ClearFocus();
  VerifySelectionHandlePositions(false);

  // Test with focus re-gained.
  widget_->GetFocusManager()->SetFocusedView(textfield_);
  VerifySelectionHandlePositions(false);
}

// Tests if the SelectRect callback is called appropriately when selection
// handles are moved.
TEST_F(TouchSelectionControllerImplTest, SelectRectCallbackTest) {
  CreateTextfield();
  textfield_->SetText(ASCIIToUTF16("textfield with selected text"));
  textfield_->SelectRange(ui::Range(3, 7));

  EXPECT_EQ(UTF16ToUTF8(textfield_->GetSelectedText()), "tfie");
  VerifySelectionHandlePositions(false);

  // Drag selection handle 2 to right by 3 chars.
  int x = textfield_->font().GetStringWidth(ASCIIToUTF16("ld "));
  SimulateSelectionHandleDrag(gfx::Point(x, 0), 2);
  EXPECT_EQ(UTF16ToUTF8(textfield_->GetSelectedText()), "tfield ");
  VerifySelectionHandlePositions(false);

  // Drag selection handle 1 to the left by a large amount (selection should
  // just stick to the beginning of the textfield).
  SimulateSelectionHandleDrag(gfx::Point(-50, 0), 1);
  EXPECT_EQ(UTF16ToUTF8(textfield_->GetSelectedText()), "textfield ");
  VerifySelectionHandlePositions(true);

  // Drag selection handle 1 across selection handle 2.
  x = textfield_->font().GetStringWidth(ASCIIToUTF16("textfield with "));
  SimulateSelectionHandleDrag(gfx::Point(x, 0), 1);
  EXPECT_EQ(UTF16ToUTF8(textfield_->GetSelectedText()), "with ");
  VerifySelectionHandlePositions(true);

  // Drag selection handle 2 across selection handle 1.
  x = textfield_->font().GetStringWidth(ASCIIToUTF16("with selected "));
  SimulateSelectionHandleDrag(gfx::Point(x, 0), 2);
  EXPECT_EQ(UTF16ToUTF8(textfield_->GetSelectedText()), "selected ");
  VerifySelectionHandlePositions(false);
}

}  // namespace views

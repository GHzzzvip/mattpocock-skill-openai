# Independent behavioral assertions

A test should disagree with broken behavior for a reason independent of the implementation.

```typescript
expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
```

The literal follows a worked example. Repeating the implementation's reduction to calculate the expected value can reproduce the same bug.

Exercise state through the interface whose contract matters. If the requirement is that a created user is retrievable, create and retrieve through that interface. Inspect storage directly only when storage behavior itself is the contract under test.

Prefer meaningful scenarios over private-method tests. Interaction assertions are appropriate when ordering or calls are externally required, not merely because today's implementation happens to make them. Multiple related assertions can describe a single behavior.

Record an observed failing run before the fix. A failed import or missing fixture does not establish that the test detects the intended defect.

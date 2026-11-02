namespace Animal
{
    public class Duck : IAnimal
    {
        private IFlyBehavior _flyBehavior;
        private IQuackBehavior _quackBehavior;
        public Duck (IFlyBehavior flyBehavior, IQuackBehavior quackBehavior)
        {
            this._flyBehavior = flyBehavior;
            this._quackBehavior = quackBehavior;
        }

        public void MakeSound()
        {
            this._quackBehavior.Quack();
        }

        public void Action()
        {
            this._flyBehavior.Fly();
        }
    }
}